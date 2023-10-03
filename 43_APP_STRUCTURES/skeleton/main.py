from fastapi import FastAPI, Response
from routers.product import product_router
from routers.categories import categories_router
from data import orders, products, Order

app = FastAPI()
app.include_router(product_router)
app.include_router(categories_router)


@app.get('/orders')
def get_orders(sort: str | None = None):
    if sort and (sort == 'asc' or sort == 'desc'):
        return sorted(orders, key=lambda p: p.delivery_date, reverse=sort == 'desc')

    return orders


@app.get('/orders/{id}')
def get_order_by_id(id: int):
    order = order_or_none(id)

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

    order.id = max(o.id for o in orders) + 1
    orders.append(order)

    return create_order_response(order)


@app.put('/orders/{id}')
def update_order(id: int, order: Order):
    existing_order = order_or_none(id)

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
    existing_order = order_or_none(id)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)

    return Response(status_code=204)


# Utility Functions


def has_missing_product_ids(ordered_product_ids: list[int]):
    valid_product_ids = [p.id for p in products]
    return any((id not in valid_product_ids) for id in ordered_product_ids)


def order_or_none(id: int):
    return next((i for i in orders if i.id == id), None)


def create_order_response(order: Order):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02
    order_products = [next(i for i in products if i.id == id) for id in order.product_ids]
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
