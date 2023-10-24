from fastapi import APIRouter
from fastapi.responses import JSONResponse

from services import products_ser
from services import profiles_ser
from services import interest_ser

from math import ceil



products_router = APIRouter(prefix='/products')



"04. View product"
@products_router.get('/{product_id}/profiles/{profile_id}')
def view_product(product_id: int, profile_id:int):
    category_id = products_ser.get_product_category(product_id)
    primary_key = (category_id, profile_id)
    # category_name = categories_ser.get_category_name(category_id)

    if not products_ser.product_exists(product_id):
        return JSONResponse(status_code=404, content={'detail': f'No product with id {product_id}'})

    if not profiles_ser.profile_exists(profile_id):
        return JSONResponse(status_code=404, content={'detail': f'No profile with id {profile_id}'})

    if not interest_ser.has_interest(category_id, profile_id):
        interest_ser.add_interest_on_category(category_id, profile_id)
        return {"message": f"Profile {profile_id} has interest on category '{category_id}' for first time."}


    current_interest = interest_ser.interests_on_category(category_id, profile_id)
    relevance = ceil(current_interest * 1.05)
    interest_ser.increase_interest(relevance, primary_key)
    new_interest = interest_ser.interests_on_category(category_id, profile_id)

    return {"message": f"Profile {profile_id} has interest {new_interest} on category {category_id}"}











