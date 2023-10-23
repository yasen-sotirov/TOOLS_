from fastapi import APIRouter
from pydantic import BaseModel




class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]

categories_router = APIRouter(prefix='/categories')