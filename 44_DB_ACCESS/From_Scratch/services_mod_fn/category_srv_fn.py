from database_mod.data_base import read_query
from database_mod.models_prj_el import Category


"ВРЪЩА ВСИЧКИ КАТЕГОРИИ"
def get_all_categories():
    data = read_query('''SELECT id, name FROM categories order by id''')

    return (Category(id=id, name=name) for id, name in data)



"ВРЪЩА КАТЕГОРИЯ ПО ID СЪС ВСИЧКИТЕ И ПРОДУКТИ"
def get_category_by_id(id: int):
    data = read_query('select id, name '
                      'from categories where id = ?', (id,))

    return next((Category(id=id, name=name) for id, name in data), None)



"СЪЩЕСТВУВА ЛИ КАТЕГОРИЯТА"
def exists(id: int):        # връща Т/F
    query = read_query(
        '''SELECT id, name 
        FROM categories
        WHERE id = ?''', (id,))
    result = any(query)





