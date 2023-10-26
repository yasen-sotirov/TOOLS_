from fastapi import FastAPI, Response
from data import Product, products, Order, orders


app = FastAPI(title='WEB services')


# опция query параметри sort search
@app.get('/products')
def get_products(
    sort: str | None = None,
    search: str | None = None):
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


# връща кода при успешна заявка
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
    return order


@app.post('/orders', status_code=201, tags=['Create new order'])
def create_order(new_order: Order):
    if new_order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')



    max_id = max(o.id for o in orders)
    new_order.id = max_id + 1

    orders.append(new_order)
    return new_order


@app.put('/orders/{id}', tags=['Update order'])
def update_order(id: int, order: Order):
    existing_order = next((o for o in orders if o.id == id), None)

    if not existing_order:
        return Response(status_code=404)

    else:
        existing_order.customer = order.customer
        existing_order.delivery_date = order.delivery_date
        existing_order.product_ids = order.product_ids

        return existing_order


@app.delete('/orders/{id}', tags=["Delete order"])
def delete_order_by_ide(id: int):
    existing_order = next((o for o in orders if o.id == id), None)

    if existing_order is None:
        return Response(status_code=404)

    orders.remove(existing_order)
    return Response(status_code=204)



