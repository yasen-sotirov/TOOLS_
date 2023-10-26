from fastapi import APIRouter, Response
from data.models import Order, OrderUpdate
from services import order_service
from services import product_service


orders_router = APIRouter(prefix='/orders')


@orders_router.get('/')
def get_orders(sort: str | None = None):
    orders = order_service.all()

    if sort and (sort == 'asc' or sort == 'desc'):
        return order_service.sort(orders, reverse=sort == 'desc')
    else:
        return orders


@orders_router.get('/{id}')
def get_order_by_id(id: int):
    order = order_service.get_with_products(id)

    return order or Response(status_code=404)


@orders_router.post('/')
def create_order(order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    products = product_service.get_many(order.product_ids)

    if len(products) < len(order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    order = order_service.create(order)

    return order_service.create_response_object(order, products)


@orders_router.put('/{id}')
def update_order(id: int, data: OrderUpdate):
    count = order_service.update(id, data)

    return {'result': f'{count} updated orders'}


@orders_router.put('/{order_id}/products')
def add_products(order_id: int, product_ids: set[int]):
    if not order_service.exists(order_id):
        return Response(status_code=404)

    current_ids = order_service.get_ordered_products(order_id)
    products_to_add = product_ids.difference(current_ids)

    if len(products_to_add) == 0:
        return {'added_product_ids': []}

    order_service.insert_products_to_order(order_id, products_to_add)

    return {'added_product_ids': products_to_add}


@orders_router.delete('/{order_id}/products')
def remove_products(order_id: int, product_ids: set[int]):
    if not order_service.exists(order_id):
        return Response(status_code=404)

    current_ids = order_service.get_ordered_products(order_id)
    products_to_delete = product_ids.intersection(current_ids)
    if len(products_to_delete) == 0:
        return {'deleted_product_ids': []}

    order_service.remove_products_from_order(order_id, products_to_delete)

    return {'deleted_product_ids': products_to_delete}


@orders_router.delete('/{id}')
def delete_order(id: int):
    order_service.delete(id)

    return Response(status_code=204)
