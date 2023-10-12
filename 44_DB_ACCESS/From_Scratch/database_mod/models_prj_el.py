from pydantic import BaseModel


class Product(BaseModel):
    id: int | None = None
    name: str
    description: str
    price: float
    category_id: int

    @classmethod
    def parse_from_query(cls, id, name, description, price, category_id):
        return cls(
            id=id,
            name=name,
            description=description,
            price=price,
            category_id=category_id)



class Category(BaseModel):
    id: int
    name: str