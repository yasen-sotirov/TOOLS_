from fastapi import FastAPI, Response
from data import Product, data


app = FastAPI()


@app.get('/products')
def get_products(
    sort=None,  # query param, optional
    search: str | None = None  # query param, optional
):
    result = data

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = next((p for p in data if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(p.id for p in data)

    product.id = max_id + 1
    data.append(product)

    return product


@app.put('/products/{id}')
def update_product(id: int, product: Product):
    existing_product = next((p for p in data if p.id == id), None)

    if existing_product is None:
        return Response(status_code=404)
    else:
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price

        return existing_product
