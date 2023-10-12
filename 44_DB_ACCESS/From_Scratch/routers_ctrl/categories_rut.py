from fastapi import APIRouter, Response
from pydantic import  BaseModel
from database_mod.models_prj_el import Category
from database_mod.models_prj_el import Product
from services_mod_fn import product_srv_fn
from services_mod_fn import category_srv_fn


category_router = APIRouter(prefix='/category')

class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]




"ВРЪЩА КАТЕГОРИЯ ПО ID"
@category_router.get('/{id}')
def get_category_by_id(id: int):
    category = category_srv_fn.get_category_by_id(id)

    # проверка дали я има тази категория
    if not category:
        # импорт от FastAPI
        return Response(status_code=404)
    else:
        result = CategoryResponseModel(
            category=category,
            products=product_srv_fn.get_products_by_category(category.id))

        return result




"ВРЪЩА ВСИЧКИ КАТЕГОРИИ И ПРОДУКТИТЕ В ТЯХ"
@category_router.get('/')
def get_all_categories():
    result = [CategoryResponseModel(
        category = category,
        product = product_srv_fn.get_products_by_category(category.id))
        for category in category_srv_fn.get_all_categories()]

    return result









