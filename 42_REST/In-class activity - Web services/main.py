from fastapi import FastAPI, Response
from data import Product, products, Order, orders
from typing import TypeVar


app = FastAPI()

@app.get('/')
def greetings():
    return {"message": "Hello to the nwe store!"}


@app.get('/products')
def get_products(sort: str | None = None, search: str | None = None):
    result = products

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)

    return product


@app.put('/products/{id}')
def update_product(id: int, product: Product):
    existing_product = next((p for p in products if p.id == id), None)

    if existing_product is None:
        return Response(status_code=404)
    else:
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price

        return existing_product


# =================================


@app.get('/orders')
def get_all_orders(sort_date: str | None = None):

    if sort_date and (sort_date == "asc" or sort_date == "desc"):
        return sorted(orders, key=lambda order: order.delivery_date, reverse= sort_date=='desc')
    return orders


@app.get('/orders/{id}')
def get_orders_by_id(id: int):
    searched_order = next((o for o in orders if o.id == id), None)

    if not searched_order:
        return {'message': "NOT FOUND"}

    else:
        ordered_products = searched_order.product_ids
        order_total = 0
        for p_id in ordered_products:
            current_product = Product.p_id
            order_total += current_product.price

        if order_total > 125:
            order_total *= 1.02

        return order_total




@app.post('/orders')
def create_order(order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content="Must contain at least one product")

    if has_missing_product_ids(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    order.id = get_next_id(orders)
    orders.append(order)

    return create_order_response(order)




@app.put('/orders/{id}')
def update_order_by_id(id: int, current_order:Order):
    existing_order = first_or_none(id, orders)

    if existing_order is None:
        return Response(status_code=404)

    if current_order == []:
        return Response(status_code=400, content="Must contain at least one product")

    if has_missing_product_ids(current_order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    # пренаписва обекта
    existing_order.product_ids = current_order.product_ids
    existing_order.delivery_date = current_order.delivery_date

    return create_order_response(existing_order)



@app.delete('/orders/{id}')
def delete_order(id: int):
    existing_order = first_or_none(id, orders)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)

    return Response(status_code=204, content="The order has been removed")



# ============== FUNCTIONS =============================

def has_missing_product_ids(ordered_product_ids: list[int]):
    valid_products_ids = [p.id for p in products]
    # ако липсва нещо ще върне True
    return any((id not in valid_products_ids) for id in ordered_product_ids )


def get_next_id(orders_list):
    return max(o.id for o in orders_list) + 1


T = TypeVar('T', Order, Product)
def first_or_none(id: int, items: list[T]) -> T:
    return next((i for i in items if i.id == id), None)


def create_order_response(order: Order):
    FREE_LIMIT = 125
    SHIPPING_FEE = 1.02
    order_products = [first_or_none(id, products) for id in order.product_ids]
    order_total = sum(p.price for p in order_products)
    if order_total > FREE_LIMIT:
        order_total *= SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery date': order.delivery_date,
        'order total': order_total
    }






































