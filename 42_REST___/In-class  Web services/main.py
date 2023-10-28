from fastapi import FastAPI, Response
from data import Product, products, Order, orders
import uvicorn
import pdb

# import logging
#
# def main() -> None:
#     logging.basicConfig(
#         level=logging.DEBUG,
#         filename='logging_file.log')
#
#     logging.debug("This is a  debug mess")
#     logging.info('This is a info mess')
#     logging.warning('This is a warning mess')
#     logging.error('This is a error mess')
#     logging.critical('This is a critical mess')
#
# if __name__ == '__main__':
#     main()



app = FastAPI(title='WEB services')

# breakpoint()
# опция query параметри sort search
@app.get('/products')
def get_products(
    sort: str | None = None,
    search: str | None = None):
    result = products
    pdb.set_trace()
    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')
    # logging.info('get products {}'.format(result))
    # print("get_products called with sort={}, search={}".format(sort, search))
    # print("and the result is:", result)
    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)
    # logging.info('get products by id {}'.format(product))
    if product is None:
        return Response(status_code=404)
    else:
        return product


# връща кода при успешна заявка
@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)
    # logging.info('post products')
    # print("Product created:", product)
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


@app.get('/orders', tags=['view orders, optional query: search by customer & sort by id'])
def get_orders(sort: str | None = None, search: str | None = None):
    result = orders

    if search:
        result = [o for o in result if (search.lower() in o.customer.lower())]

    if sort and (sort=='asc' or sort=='desc'):
        result = sorted(result, key=lambda o: o.id , reverse=sort == 'desc')

    return result


@app.get('/orders/{id}', tags=['Get order by id'])
def get_order_by_id(id: int):
    # търси ордера в списъка с ордери
    order = next((o for o in orders if o.id == id), None)

    if order is None:
        return Response(status_code=404)
    return create_order_response(order)


@app.post('/orders', status_code=201, tags=['Create new order'])
def create_order(new_order: Order):
    if new_order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    max_id = max(o.id for o in orders)
    new_order.id = max_id + 1

    orders.append(new_order)
    return create_order_response(new_order)


@app.put('/orders/{id}', tags=['Update order'])
def update_order(id: int, order: Order):
    existing_order = next((o for o in orders if o.id == id), None)

    if not existing_order:
        return Response(status_code=404, content='Must contain at least one product')

    if order.product_ids == []:
        return Response(status_code=404, content='Must contain existing product')

    existing_order.customer = order.customer
    existing_order.delivery_date = order.delivery_date
    existing_order.product_ids = order.product_ids

    return create_order_response(order)


@app.delete('/orders/{id}', tags=["Delete order"])
def delete_order_by_ide(id: int):
    existing_order = next((o for o in orders if o.id == id), None)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)
    return Response(status_code=204)




from typing import TypeVar

T_var = TypeVar("T_var", Product, Order)

def first_or_none(id: id, items: list [T_var]) -> T_var:
    return next((item for item in items if item.id == id), None)


def create_order_response(order: Order):
    free_shipping_limit = 125
    shipping_fee = 1.05
    order_products = [first_or_none(id, products) for id in order.product_ids]
    order_total = sum(p.price for p in order_products)
    if order_total > free_shipping_limit:
        order_total *= shipping_fee

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery_date': order.delivery_date,
        'order_total': order_total}



def has_missing_product_ids(ordered_product_ids: list[int]):
    valid_product_ids = [p.id for p in products]
    return any((id not in valid_product_ids) for id in ordered_product_ids)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)