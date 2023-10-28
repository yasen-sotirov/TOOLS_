from fastapi import APIRouter, Response
from data import Product
from services import product_service
from services import category_service


product_router = APIRouter(prefix='/products')


@product_router.get('/')
def get_products(
    sort: str | None = None,
    sort_by: str | None = None,
    search: str | None = None
):
    result = product_service.all(search)

    if sort and (sort == 'asc' or sort == 'desc'):
        return product_service.sort(result, reverse=sort == 'desc', attribute=sort_by)
    else:
        return result


@product_router.get('/{id}')
def get_product_by_id(id: int):
    product = product_service.get_by_id(id)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@product_router.post('/', status_code=201)
def create_product(product: Product):
    if not category_service.exists(product.category_id):
        return Response(status_code=400,
                        content=f'Category {product.category_id} does not exist')

    return product_service.create(product)


@product_router.put('/{id}')
def update_product(id: int, product: Product):
    if not category_service.exists(product.category_id):
        return Response(status_code=400,
                        content=f'Category {product.category_id} does not exist')

    existing_product = product_service.get_by_id(id)
    if existing_product is None:
        return Response(status_code=404)
    else:
        return product_service.update(existing_product, product)
