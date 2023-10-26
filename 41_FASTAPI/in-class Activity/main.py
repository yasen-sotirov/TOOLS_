from fastapi import FastAPI, Response
from data import Product, products
import uvicorn

# https://fastapi.tiangolo.com/tutorial/

app = FastAPI(title="In-Class Activity", debug=True)


@app.get("/", tags=["root"])
def root():
    return {"message": "Welcome screen"}


@app.get('/products', tags=['search products'])
def get_products(sort: str | None = None, search: str | None = None):
    result = products

    if search:
        # търси по ключова дума
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result



@app.get('/products/{id}', tags=['view products by id'])
def get_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product



@app.put('/products/{id}', tags = ['update product by id'])
def update_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product




@app.delete('/products/{id}', tags=['delete product by id'])
def delete_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        products.remove(product)
        return {"message": "product deleted"}


# връща зададен от нас код
@app.post('/products', status_code=201, tags=['crete product'])
def create_product(product: Product):
    # взима най-голямото id
    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)

    return product


@app.put('/products/{id}', tags=['update product'])
def update_product(id: int, updated_product: Product):
    for current_product in products:
        if current_product.id == id:
            current_product.price = updated_product.price
            current_product.name = updated_product.name
            current_product.description = updated_product.description
            return {"product": current_product}
    return {"massage": "The product not found"}





if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



