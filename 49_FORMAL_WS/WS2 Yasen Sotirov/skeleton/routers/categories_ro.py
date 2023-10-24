from fastapi import APIRouter
from services.categories_ser import all_categories



categories_router = APIRouter(prefix='/categories')


"06. Get categories"
@categories_router.get('/')
def get_all_categories():
    return all_categories()








