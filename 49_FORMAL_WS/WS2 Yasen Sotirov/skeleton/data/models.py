from pydantic import BaseModel, constr, conint



"=== PROFILE ==="
class Profile(BaseModel):
    id: int | None
    ip_address: str
    country_code: str

    @classmethod
    def from_query_result(cls, id, ip_address, country_code):
        return cls(
            id=id,
            ip_address=ip_address,
            country_code=country_code)


    @classmethod
    def country_codes(cls, code):
        return cls(code=code)


"=== CATEGORY ==="
class Category(BaseModel):
    id: int
    name: str
    relevance: int

    @classmethod
    def from_query(cls, id, name):
        return cls(id=id, name=name)



"=== INTEREST ==="
class Interest(BaseModel):
    profile_id: int
    category_id: int
    relevance: int




"=== PRODUCT ==="
class Product(BaseModel):
    id: int | None
    name: str
    price: float
    category_id: int

    @classmethod
    def from_query_to_obj(cls, id, name, price, category_id):
        return cls(
            id=id,
            name=name,
            price=price,
            category_id=category_id)


















