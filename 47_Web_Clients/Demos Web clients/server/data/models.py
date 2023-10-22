from datetime import date
from pydantic import BaseModel, constr


class Category(BaseModel):
    id: Optional[int]
    name: str


class Product(BaseModel):
    id: Optional[int]
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
    id: Optional[int]
    product_ids: list[int] = []
    delivery_date: date
    delivery_address: str
    user_id: int

    @classmethod
    def from_query_result(cls, id, delivery_date, delivery_address, user_id=None, product_ids=[]):
        return cls(
            id=id,
            delivery_date=delivery_date,
            delivery_address=delivery_address,
            user_id=user_id,
            product_ids=product_ids)


class OrderUpdate(BaseModel):
    delivery_date: date
    delivery_address: str


class Role:
    CUSTOMER = 'customer'
    ADMIN = 'admin'


TUsername = constr(regex='^\w{2,30}$')


class User(BaseModel):
    id: Optional[int]
    username: TUsername
    password: str
    role: str

    def is_admin(self):
        return self.role == Role.ADMIN

    @classmethod
    def from_query_result(cls, id, username, password, role):
        return cls(
            id=id,
            username=username,
            password=password,
            role=role)


class LoginData(BaseModel):
    username: TUsername
    password: str


class UserResponse(BaseModel):
    id: Optional[int]
    username: str


class OrderResponse(BaseModel):
    id: Optional[int]
    customer: UserResponse
    products: list[Product]
    delivery_date: date
    delivery_address: str
    order_total: float
