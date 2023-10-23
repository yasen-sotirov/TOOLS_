from fastapi import APIRouter
from pydantic import BaseModel
from data.models import Category, Product
from data.database import read_query



class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]


def get_category_name(id: int):
    return read_query('''SELECT name FROM categories WHERE id = ?''', (id,))




