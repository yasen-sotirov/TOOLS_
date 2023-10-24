from data.database import read_query, query_count


def product_exists(id: int):
    return query_count('''SELECT COUNT(*) from products WHERE id = ?''',
                       (id,)) > 0



def get_product_category(product_id: int):
    return read_query('''SELECT category_id 
                        FROM products
                        WHERE id = ?''', (product_id,))