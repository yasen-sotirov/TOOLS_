from datetime import date
from pydantic import BaseModel


class Category(BaseModel):
    id: int | None
    name: str


class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float
    category_id: int

    @classmethod
    def from_query_result(cls, id, name, description, price, category_id):
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category_id=category_id)


class Order(BaseModel):
    id: int | None
    customer: str
    product_ids: list[int]
    delivery_date: date
