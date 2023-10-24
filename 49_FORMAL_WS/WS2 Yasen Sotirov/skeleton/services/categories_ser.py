from pydantic import BaseModel
from data.models import Category, Product
from data.database import read_query



class CategoryResponseModel(BaseModel):
    category: Category
    products: list[Product]




def all_categories():
    data = read_query('''SELECT id, name FROM categories''')

    return (Category.from_query(*row) for row in data)




def get_category_name(id: int):
    result = read_query('''SELECT name FROM categories 
                            WHERE id = ?''',(id,))
    return result



