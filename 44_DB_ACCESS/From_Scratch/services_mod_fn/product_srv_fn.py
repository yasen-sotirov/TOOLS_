from database_mod.models_prj_el import Product
from database_mod.data_base import read_query, insert_query



"ВЗИМА ВСИЧКИ ПРОДУКТИ ИЛИ ТЪРСИ ПО ИМЕ"
def get_all(search_by_name: str | None = None):

    # ако не търси по име
    if search_by_name is None:
        data = read_query(
            '''SELECT id, name, description, price, category_id
            FROM products''')

    else:   # ако търси по име
        data = read_query(
            '''SELECT id, name, description, price, category_id
            FROM products
            WHERE name LIKE ?''', (f"%{search_by_name}%",))
                                            # важна (,)
    result = (Product.parse_from_query(* row) for row in data)
    return result




"СОРТИРАНЕ"
        # сортира по подразбиране параметър "цена“
def sort(product: list[Product], *, param="price"):
    if param == "price":
        def sort_fn(p: Product):
            result = p.price
            return result

    elif param == "name":
        def sort_fn(p: Product):
            result = p.name
            return result

    else:
        def sort_fn(p: Product):
            result = p.id
            return result

    result = sorted(product, key=sort_fn)
    return result




"ВРЪЩА ПРОДУКТИТЕ ПО КАТЕГОРИЯ"
def get_products_by_category(category_id: int):
    data = read_query(
        '''SELECT id, name, description, price, category_id
        FROM products
        WHERE category_id = ?''', (category_id,)) #важна запетайка

    result = (Product.parse_from_query(*row) for row in data)
    return result



"СЪЗДАВА ПРОДУКТ"
def create_product(product: Product):
    generated_id = insert_query(
        '''SELECT INTO products(name, description, price, category_id)
        VALUES(?,?,?,?)''',
        (product.name, product.description, product.price, product.category_id))

    product.id = generated_id
    return product



















