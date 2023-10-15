from sqlite3 import IntegrityError
from common.responses import BadRequest
from data.database import insert_query, read_query, update_query
from data.models import Developer, DeveloperDB, Level


def all(filters: dict):
    sql = 'SELECT id, name, level FROM devs WHERE 1=1'
    sql_params = []

    for column, value in filters.items():
        if column == 'name':
            sql += f' and {column} like ?'
            sql_params.append(f'%{value}%')
        else:
            sql += f' and {column} = ?'
            sql_params.append(value)

    data = read_query(sql, tuple(sql_params))

    return (Developer.from_query_result(*row) for row in data)


def get_by_id(id: int):
    data = read_query('''SELECT d.id, d.name, d.level,GROUP_CONCAT(p.project_id) AS project_ids
                                    FROM devs d LEFT JOIN devs_projects p ON d.id = p.dev_id
                                    WHERE d.id = ? GROUP BY d.id
                                    ''', (id,))

    return next((DeveloperDB.from_query_result(*row) for row in data), None)


def create(developer: Developer):
    try:
        level = Level.from_string(developer.level)
        level = level.value[0]
    except ValueError:
        return BadRequest(content=f"Developer's level {developer.level} is not valid")

    try:
        generated_id = insert_query('INSERT INTO devs(name,level) VALUES(?,?)', (developer.name, level))
    except IntegrityError:
        return BadRequest(content=f'Developer {developer.name} already exists')

    developer.id = generated_id

    return developer
