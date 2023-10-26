from fastapi import FastAPI, Response
from data import Order, Product, products, orders
from typing import TypeVar


app = FastAPI()


@app.get('/products')
def get_products(
    sort: str | None = None,
    search: str | None = None
):
    result = products

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = first_or_none(id, products)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@app.post('/products', status_code=201)
def create_product(product: Product):
    product.id = get_next_id(products)
    products.append(product)

    return product


@app.put('/products/{id}')
def update_product(id: int, product: Product):
    existing_product = first_or_none(id, products)

    if existing_product is None:
        return Response(status_code=404)
    else:
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price

        return existing_product


@app.get('/orders')
def get_orders(sort: str | None = None):
    if sort and (sort == 'asc' or sort == 'desc'):
        return sorted(orders, key=lambda p: p.delivery_date, reverse=sort == 'desc')

    return orders


@app.get('/orders/{id}')
def get_order_by_id(id: int):
    order = first_or_none(id, orders)

    if order is None:
        return Response(status_code=404)
    else:
        return create_order_response(order)


@app.post('/orders')
def create_order(order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if has_missing_product_ids(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    order.id = get_next_id(orders)
    orders.append(order)

    return create_order_response(order)


@app.put('/orders/{id}')
def update_order(id: int, order: Order):
    existing_order = first_or_none(id, orders)

    if existing_order is None:
        return Response(status_code=404)

    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if has_missing_product_ids(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    existing_order.product_ids = order.product_ids
    existing_order.delivery_date = order.delivery_date

    return create_order_response(existing_order)


@app.delete('/orders/{id}')
def delete_order(id: int):
    existing_order = first_or_none(id, orders)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)

    return Response(status_code=204)





"UTILITY FUNCTIONS"


def get_next_id(seq: list):
    max_id = max(item.id for item in seq)

    return max_id + 1


def has_missing_product_ids(ordered_product_ids: list[int]):
    valid_product_ids = [p.id for p in products]
    return any((id not in valid_product_ids) for id in ordered_product_ids)


T = TypeVar('T', Order, Product)


def first_or_none(id: int, items: list[T]) -> T:
    return next((i for i in items if i.id == id), None)


def create_order_response(order: Order):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02
    order_products = [first_or_none(id, products) for id in order.product_ids]
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
