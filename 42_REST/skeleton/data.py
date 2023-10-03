from pydantic import BaseModel
from datetime import date

class Product(BaseModel):   # Model продукти
    id: int | None
    name: str
    description: str
    price: float


products = [
    Product(id=1, name='TV', description='LCD 40 Inch', price = 749.99),
    Product(id=2, name='Laptop', description='2x2.6 GHz CPU; 6GB RAM; HD Graphics', price = 699.99),
    Product(id=3, name='Smartphone', description='6.55" HD+, 5G', price = 1349.90),
    Product(id=4, name='Keyboard', description='Full-size Layout, Mechanical', price = 99.00),
]


class Order(BaseModel):     # Model поръчки
    id: int |None
    customer: str
    products_ids: list[int]
    delivery_date: date


orders = [
    Order(
        id = 1,
        customer='Steven',
        product_ids=[2,4],
        delivery_date=date(2025, 2, 8)
    ),
    Order(
        id = 2,
        customer='Alice',
        product_ids=[1],
        delivery_date=date(2023, 8, 4)
    )
]