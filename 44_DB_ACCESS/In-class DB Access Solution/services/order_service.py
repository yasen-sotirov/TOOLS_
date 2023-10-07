from data.database import insert_query, read_query, update_query
from data.models import Order, OrderUpdate, Product


def all():
    data = read_query('''SELECT id, customer, delivery_date, delivery_address, product_id 
                         FROM orders AS o 
                           LEFT JOIN orders_products AS op 
                             ON o.id = op.order_id''')

    flattened = {}
    for id, customer, delivery_date, delivery_address, product_id in data:
        if id not in flattened:
            flattened[id] = (id, customer, delivery_date, delivery_address, [])

        if product_id is not None:
            flattened[id][-1].append(product_id)

    return (Order.from_query_result(*obj) for obj in flattened.values())


def sort(lst: list[Order], reverse=False):
    return sorted(
        lst,
        key=lambda p: p.delivery_date,
        reverse=reverse)


def get_with_products(id: int):
    order_data = read_query(
        'select id, customer, delivery_date, delivery_address from orders where id = ?', (id,))
    order = next((Order.from_query_result(*row) for row in order_data), None)

    if order is None:
        return None

    products_data = read_query(
        '''SELECT p.id, p.name, p.description, p.price, p.category_id
               FROM products p
               WHERE p.id in (SELECT product_id
                              FROM orders_products
                              WHERE order_id = ?)''',
        (order.id,))

    return create_response_object(
        order,
        [Product.from_query_result(*row) for row in products_data])


def create(order: Order):
    generated_id = insert_query(
        'INSERT INTO orders(customer,delivery_date,delivery_address) VALUES(?,?,?)',
        (order.customer, order.delivery_date, order.delivery_address))

    order.id = generated_id

    insert_products_to_order(order.id, order.product_ids)

    return order


def exists(order_id: int):
    data = read_query('SELECT 1 from orders where id = ?', (order_id,))

    return len(data) > 0


def get_ordered_products(order_id: int) -> set[int]:
    data = read_query(
        'SELECT product_id from orders_products where order_id = ?', (order_id,))

    return set(i[0] for i in data)


def update(order_id: int, order: OrderUpdate):
    result = update_query(
        '''UPDATE orders SET
           delivery_date = ?, delivery_address = ?
           WHERE id = ? 
        ''',
        (order.delivery_date, order.delivery_address, order_id))

    return result


def delete(order_id):
    update_query('DELETE FROM orders_products WHERE order_id = ?', (order_id,))
    update_query('DELETE FROM orders WHERE id = ?', (order_id,))


def insert_products_to_order(order_id: int, product_ids: list[int]):
    relations = ','.join(
        f'({order_id},{product_id})' for product_id in product_ids)

    insert_query(
        f'INSERT INTO orders_products(order_id, product_id) VALUES {relations}')


def remove_products_from_order(order_id: int, product_ids: list[int]):
    ids_to_delete = ','.join(str(p_id) for p_id in product_ids)

    insert_query(
        f'''DELETE FROM orders_products 
            WHERE order_id = ? and product_id IN ({ids_to_delete})''',
        (order_id,))


def create_response_object(order: Order, order_products: list[Product]):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02

    order_total = sum(p.price for p in order_products)
    if order_total > FREE_SHIPPING_LIMIT:
        order_total = order_total * SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery_date': order.delivery_date,
        'delivery_address': order.delivery_address,
        'order_total':  round(order_total, 2)
    }
