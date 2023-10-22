from datetime import date
from pydantic import BaseModel, constr

"====== CATEGORY ====="


class Category(BaseModel):
    id: int | None
    name: str


" ===== PRODUCT ====="


class Product(BaseModel):
    id: int | None
    name: str
    description: str
    price: float
    category_id: int

    @classmethod  # асоциира се с класа, а не с инстанция на класа:
    def from_query_result_to_obj(cls, id, name, description, price, category_id):
        # cls създава нова инстанция на класа
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category_id=category_id)


"====== USERS ========"


class Role:
    CUSTOMER = "customer"
    ADMIN = "admin"


TUsername = constr(pattern='^\w{2,30}$')


class User(BaseModel):
    id: int | None
    username: TUsername
    password: str
    role: str

    @classmethod
    def from_query_result(cls, id, username, password, role):
        return cls(
            id=id,
            username=username,
            password=password,
            role=role)

    def is_admin(self):
        return self.role == Role.ADMIN


"===== ORDER ======"


class Order(BaseModel):
    id: int | None
    product_ids: list[int] = []
    delivery_date: date
    delivery_address: str | None
    user_id: int | None

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
    delivery_address: str | None


class OrderResponse(BaseModel):
    id: int
    customer: User
    products: list[Product]
    delivery_date: date
    delivery_address: str | None
    order_total: float


class LoginData(BaseModel):
    username: TUsername
    password: str
