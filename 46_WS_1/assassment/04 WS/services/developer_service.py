from data.database import read_query, insert_query
from data.models import Developer, Project

dev_levels = {"junior": 1, "mid": 2, "senior": 3, 1: "junior", 2: "mid", 3: "senior"}


def all(search: str = None, searchlevel: str = None):
    if search:
        data = read_query('SELECT id, name, level FROM devs WHERE name LIKE ?', (f'%{search}%', ))
    elif searchlevel:
        data = read_query('SELECT id, name, level FROM devs WHERE level LIKE ?', (dev_levels[searchlevel],))
    else:
        data = read_query('SELECT id, name, level from devs')

    return (Developer(id=id, name=name,level=dev_levels[level]) for id, name, level in data)


def get_dev_by_id(id: int):
    data = read_query('SELECT name, level from devs WHERE id = ?', (id,))
    return next((Developer(id=id, name=name, level=dev_levels[level]) for name, level in data), None)


def create_dev(dev: Developer):
    level = dev_levels[dev.level]
    generated_id = insert_query(
        'INSERT INTO devs(name,level) VALUES(?,?)',
        (dev.name, level))
    dev.id = generated_id
    return dev


def create_response(dev: Developer, projects: list[Project]):
    return {
        'id': dev.id,
        'name': dev.name,
        'level': dev_levels[dev.level],
        'projects': projects
    }


def get_devs_by_project(id: int):
    data = read_query(
        '''SELECT d.id, d.name, d.level
                FROM devs d
                WHERE d.id in (SELECT dev_id
                                FROM devs_projects
                                WHERE project_id = ?)''', (id,))
    return [Developer(id=id, name=name, level=dev_levels[level]) for id,name,level in data]