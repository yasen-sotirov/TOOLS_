from fastapi import APIRouter, Query, Response
from fastapi.responses import JSONResponse
from data.models import Dev, Project, DEV_LEVEL
from data.database import read_query, query_count, insert_query


devs_router = APIRouter(prefix='/devs')

"2. Get all devs"
@devs_router.get('/')
def get_devs(name: str | None = None,
             level: str | None = Query(default=None, regex='^junior|mid|senior$')):

    sql = 'SELECT id, name, level FROM devs'
    where_clause = []

    if name:
        where_clause.append(f"name like '%{name}%'")
    if level:
        where_clause.append(f"level = {DEV_LEVEL[level]}")

    if where_clause:
        sql += ' WHERE ' + ' AND '.join(where_clause)
    data = read_query(sql)

    return (Dev.from_query_result(*row) for row in data)





"4. Get dev by id"
@devs_router.get('/{id}')
def get_dev_by_id(id: int):
    dev_data = read_query('SELECT id, name, level WHERE id = ?',
                      (id,))
    if dev_data is None: return None

    project_data = read_query('''SELECT id, name, is_open, team_limit FROM projects
                                join devs_project WHERE dev_id = ?''',
                              (id,))

    dev_projects = [Project.from_query_result(*row) for row in project_data]

    return Dev.from_query_result(*dev_data[0], dev_projects)



"6. Create dev"
@devs_router.post('/', status_code=201)
def create_dev(dev: Dev):
    name_exists = query_count('SELECT COUNT(*) FROM devs WHERE name = ?',
                              (Dev.name,)) > 0
    if name_exists:
        return JSONResponse(status_code=409,
                            content={'message': 'Dev name must be unique'})

    generated_id = insert_query('INSERT INTO devs(name, level) VALUE(?,?)',
                                (dev.name, DEV_LEVEL[dev.level]))
    dev.id = generated_id
    return dev






def dev_id_exists(id: int):
    return query_count('SELECT COUNT(*) FROM devs WHERE id = ?',
                       (id,)) > 0




