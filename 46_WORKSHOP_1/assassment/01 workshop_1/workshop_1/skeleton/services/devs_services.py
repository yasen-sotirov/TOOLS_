from data.models import Devs
from data.database import insert_query, read_query, update_query, init_database


def all(search: str = None, level: int = None):

    level_mapping = {1: "junior", 2: "mid", 3: "senior"}

    if search is None and level is None:
        data = read_query(
            '''SELECT id, name, level
               FROM devs''')
    elif search != None and level is None:
        data = read_query(
            '''SELECT id, name, level
               FROM devs 
               WHERE name LIKE ?''', (f'%{search}%',))
    elif level != None and search is None:
        data = read_query(
            '''SELECT id, name, level
               FROM devs 
               WHERE level == ?''', (level, ))
        
    result = []
    for row in data:
        dev = Devs.from_query_result(*row)
        if dev.level in level_mapping:
            dev.level = level_mapping[dev.level]
        result.append(dev)

    return result


def get_by_id(id: int):
    
    data = read_query(
    '''SELECT d.id AS dev_id, d.name AS dev_name, d.level AS dev_level, p.id AS project_id, p.name AS project_name, p.is_open AS project_status, p.team_limit AS project_limit
       FROM devs AS d
       LEFT JOIN devs_projects AS dp ON d.id = dp.dev_id
       LEFT JOIN projects AS p ON dp.project_id = p.id
       WHERE d.id = ?''', (id,))

    dev = None
    projects = []

    for row in data:
        if dev is None:
            dev = {
                "id": row[0],
                "name": row[1],
                "level": row[2]
            }

            level_mapping = {1: "junior", 2: "mid", 3: "senior"}
            if dev["level"] in level_mapping:
                dev["level"] = level_mapping[dev["level"]]
        if row[3] is not None:
            project = {
                "id": row[3],
                "name": row[4],
                "status": row[5],
                "limit": row[6]
            }
            projects.append(project)

    if dev is not None:
        dev["projects"] = projects
        return dev

    return None


def sort(devs: list[Devs], *, attribute='filter_by_name', reverse=False):
    if attribute == 'filter_by_name':
        def sort_fn(d: Devs): return d.name
    elif attribute == 'filter_by_exp':
        def sort_fn(d: Devs): return d.level
    
    return sorted(devs, key=sort_fn, reverse=reverse)


def create(dev: Devs):
    generated_id = insert_query(
        'INSERT INTO devs(id,name,level) VALUES(?,?,?)',
        (dev.id, dev.name, dev.level))

    dev.id = generated_id
    return dev