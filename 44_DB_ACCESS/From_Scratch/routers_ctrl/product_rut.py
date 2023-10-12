from fastapi import APIRouter, Response
from services_mod_fn import product_srv_fn
from services_mod_fn import category_srv_fn
from database_mod.models_prj_el import Product


product_router = APIRouter(prefix='/products')




"ВРЪЩА ВСИЧКИ ПРОДУКТИ"
@product_router.get('/')
def get_all_products(
        sort: str | None = None,
        sort_by: str | None = None,
        search_by_name: str | None = None):

    # от файла вземам функцията
    result = product_srv_fn.get_all(search_by_name)

    if sort and (sort == "asc" or sort =="desc"):
        return product_srv_fn.sort(result, reverse=sort == 'desc', attribute=sort_by)
    else:
        return result



"СЪЗДАВА ПРОДУКТ"
@product_router.post('/')
def create_product(product: Product):
    category_exists = category_srv_fn.exists(product.category_id)

    if not category_exists:
        return Response(status_code=400,
                        content=f'Category {product.category_id} does not exist')

    result = product_srv_fn.create_product(product)
    return result










