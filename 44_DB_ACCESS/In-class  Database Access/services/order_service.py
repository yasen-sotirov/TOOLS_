from data.models import Order
from data.in_memory import orders
from services import product_service
from data.database import read_query


def all():
    data = read_query('''SELECT id, customer, delivery_date, delivery_address, product_id 
                         FROM orders AS o 
                         LEFT JOIN orders_products AS o_p 
                         ON o.id = o_p.order_id''')

    flattened = {}
    for id, customer, delivery_date, delivery_address, product_id in data:
        if id not in data:
            flattened[id] = (id, customer, delivery_date, delivery_address, [])

        if product_id is not None:
            flattened[id][-1].append(product_id)

    return  (Order.from_query_result(*obj) for obj in flattened.values())




def sort(lst: list[Order], reverse=False):
    return sorted(
        lst,
        key=lambda p: p.delivery_date,
        reverse=reverse)


def get_by_id(id: int):
    order_data = read_query('''SELECT id, customer, delivery_date, delivery_address 
                                FROM orders WHERE id = ?''',
                            (id,))






def create(order: Order):
    order.id = max(o.id for o in orders) + 1
    orders.append(order)

    return order

def update(old: Order, new: Order):
    old.product_ids = new.product_ids
    old.delivery_date = new.delivery_date

    return old

def delete(order):
    orders.remove(order)

def create_response_object(order: Order):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02

    order_products = [product_service.get_by_id(id)
                      for id in order.product_ids]

    order_total = sum(p.price for p in order_products)
    if order_total > FREE_SHIPPING_LIMIT:
        order_total = order_total * SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery_date': order.delivery_date,
        'order_total':  order_total
    }
