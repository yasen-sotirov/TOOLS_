from data.database import read_query, insert_query, update_query
from data.models import Project, Developer

statuses = {0: "closed", 1: "open", "closed": 0, "open": 1}


def all(search: str = None, searchlimit: int = None, searchstatus: str = None):
    if search:
        data = read_query('SELECT id, name, is_open, team_limit FROM projects WHERE name LIKE ?', (f'%{search}%', ))
    elif searchlimit:
        data = read_query('SELECT id, name, is_open, team_limit FROM projects WHERE team_limit <= ?', (searchlimit,))
    elif searchstatus:
        data = read_query('SELECT id, name, is_open, team_limit '
                          'FROM projects WHERE is_open =?', (statuses[searchstatus], ))
    else:
        data = read_query('SELECT id, name, is_open, team_limit from projects')

    return (Project(id=id, name=name,status=statuses[is_open], limit=team_limit)
            for id, name, is_open, team_limit in data)


def get_project_by_id(id: int):
    data = read_query('SELECT name, is_open, team_limit FROM projects WHERE id =?', (id,))
    return next(
        (Project(id=id, name=name, status=statuses[is_open], limit=team_limit) for name, is_open, team_limit in data),
        None)


def create_project(project: Project):
    status = statuses[project.status]
    generated_id = insert_query(
        'INSERT INTO projects(name, is_open, team_limit) VALUES (?,?,?)', (project.name, status, project.limit))
    project.id = generated_id
    return project


def update_status(id, status):
    project = get_project_by_id(id)

    result = update_query(
        '''UPDATE projects SET
           is_open = ? WHERE id = ?''',
        (statuses[status.status], id))

    if result > 0:
        project.status = status.status
        return project


def create_response(project: Project, devs: list[Developer]):
    return {
        'id': project.id,
        'name': project.name,
        'status': statuses[project.status],
        'limit': project.limit,
        'developers': devs
    }


def get_projects_by_dev(id: int):
    data = read_query(
        '''SELECT p.id, p.name, p.is_open, p.team_limit
                FROM projects p
                WHERE p.id in (SELECT project_id
                                FROM devs_projects
                                WHERE dev_id = ?)''', (id,))
    return [Project
            (id=id, name=name, status=statuses[is_open], limit=team_limit) for id, name, is_open, team_limit in data]


def assign_dev_to_project(id: int, dev_id: int):
    return insert_query('INSERT INTO devs_projects(dev_id, project_id) VALUES(?,?)', (dev_id, id))


def delete_def_from_project(id: int, dev_id: int):
    update_query('DELETE FROM devs_projects WHERE dev_id =? AND project_id =?', (id, dev_id))

