from data.models import Product
from data.database import insert_query, read_query, update_query


def all(search: str = None):
    if search is None:
        data = read_query(
            '''SELECT id, name, description, price, category_id
               FROM products''')
    else:
        data = read_query(
            '''SELECT id, name, description, price, category_id
               FROM products 
               WHERE name LIKE ?''', (f'%{search}%',))

    return (Product.from_query_result(*row) for row in data)


def get_by_id(id: int):
    data = read_query(
        '''SELECT id, name, description, price, category_id
            FROM products 
            WHERE id = ?''', (id,))

    return next((Product.from_query_result(*row) for row in data), None)


def get_many(ids: list[int]):
    ids_joined = ','.join(str(id) for id in ids)
    data = read_query(f'''
            SELECT id, name, description, price, category_id
            FROM products 
            WHERE id IN ({ids_joined})''')

    return [Product.from_query_result(*row) for row in data]


def get_by_category(category_id: int):
    data = read_query(
        '''SELECT id, name, description, price, category_id
            FROM products 
            WHERE category_id = ?''', (category_id,))

    return (Product.from_query_result(*row) for row in data)


def sort(products: list[Product], *, attribute='price', reverse=False):
    if attribute == 'price':
        def sort_fn(p: Product): return p.price
    elif attribute == 'name':
        def sort_fn(p: Product): return p.name
    else:
        def sort_fn(p: Product): return p.id

    return sorted(products, key=sort_fn, reverse=reverse)


def create(product: Product):
    generated_id = insert_query(
        'INSERT INTO products(name,description,price,category_id) VALUES(?,?,?,?)',
        (product.name, product.description, product.price, product.category_id))

    product.id = generated_id

    return product


def update(old: Product, new: Product):
    merged = Product(
        id=old.id,
        name=new.name or old.name,
        description=new.description or old.description,
        price=new.price or old.price,
        category_id=new.category_id or old.category_id)

    update_query(
        '''UPDATE products SET
           name = ?, description = ?, price = ?, category_id = ?
           WHERE id = ? 
        ''',
        (merged.name, merged.description, merged.price, merged.category_id, merged.id))

    return merged

def delete(product_id: int):
    update_query('DELETE FROM orders_products WHERE product_id = ?', (product_id,))
    update_query('DELETE FROM products WHERE id = ?', (product_id,))