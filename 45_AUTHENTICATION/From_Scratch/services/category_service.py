from data.database import read_query, insert_query
from data.models import Category


def all_categories():
    data = read_query('SELECT id, name FROM categories ORDER BY id')

    return (Category(id=id, name=name) for id, name in data)


def get_category_by_id(id: int):
    data = read_query('SELECT id, name FROM categories WHERE id = ?', (id,))

    return next((Category(id=id, name=name) for id, name in data))


def create_category(category: Category):
    generated_id = insert_query('INSERT INTO categories(name) values(?)',
                                (category.name,))

    category.id  = generated_id

    return category








