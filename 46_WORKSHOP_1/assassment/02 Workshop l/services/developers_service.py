from data.database import read_query, insert_query
from data.models import Developer, Project, DeveloperCreate

level_mapping = {'junior': 1, 'mid': 2, 'senior': 3}


def get_all(name: str = None, level: str = None):
    lvl = level_mapping.get(level)
    base_query = "SELECT * FROM devs WHERE 1=1"
    query_params = []

    if name:
        base_query += " AND name LIKE ?"
        query_params.append(f'{name}%')

    if lvl is not None:
        base_query += " AND level = ?"
        query_params.append(lvl)

    data = read_query(base_query, tuple(query_params))
    return (Developer.from_query_result(*row) for row in data)


def get_by_id_with_projects(id: int):
    developer = get_by_id(id)

    if developer is None:
        return None

    projects = get_projects_for_dev(developer)

    return create_response_object(
        developer,
        [Project.from_query_result(*p) for p in projects])


def get_by_id(id: int):
    dev_data = read_query(
        '''SELECT * FROM devs WHERE id = ?''', (id,))

    return next((Developer.from_query_result(*row) for row in dev_data), None)


def get_projects_for_dev(developer: Developer):
    projects_data = read_query(
        '''SELECT p.id, p.name, p.is_open as status, p.team_limit FROM projects p
           WHERE p.id IN (SELECT project_id FROM devs_projects WHERE dev_id = ?)''',
        (developer.id,))

    return projects_data


def create(developer: DeveloperCreate):
    generated_id = insert_query(
        '''INSERT INTO devs(name, level) VALUES(?, ?)''', (developer.name, developer.level))

    developer.id = generated_id
    return developer


def create_response_object(developer: Developer, projects: list[Project]):
    return {
        'id': developer.id,
        'name': developer.name,
        'level': developer.level,
        'projects': projects
    }
