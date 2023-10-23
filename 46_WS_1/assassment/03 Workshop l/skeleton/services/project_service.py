from sqlite3 import IntegrityError

from common.responses import BadRequest
from data.database import insert_query, read_query, update_query
from data.models import Project, ProjectDB, Status, ProjectUpdate


def all(filters: dict):
    sql = 'SELECT id, name, is_open, team_limit FROM projects WHERE 1=1'
    sql_params = []

    for column, value in filters.items():
        if column == 'name':
            sql += f' and {column} like ?'
            sql_params.append(f'%{value}%')
        elif column == 'team_limit':
            sql += f' and {column} <= ?'
            sql_params.append(value)
        else:
            sql += f' and {column} = ?'
            sql_params.append(value)

    data = read_query(sql, tuple(sql_params))

    return (Project.from_query_result(*row) for row in data)


def get_by_id(id: int, db=False):
    if db:
        data = read_query('''SELECT p.id, p.name, p.is_open, p.team_limit, GROUP_CONCAT(d.dev_id) AS developer_ids
                                        FROM projects p LEFT JOIN devs_projects d ON p.id = d.project_id
                                        WHERE p.id = ? GROUP BY p.id
                                        ''', (id,))

        return next((ProjectDB.from_query_result(*row) for row in data), None)

    data = read_query('SELECT id, name, is_open, team_limit FROM projects WHERE id = ?', (id,))

    return next((Project.from_query_result(*row) for row in data), None)


def create(project: Project):
    try:
        status = Status.from_string(project.status)
        status = status.value[0]
    except ValueError:
        return BadRequest(content=f"Project's status {project.status} is not valid")

    try:
        generated_id = insert_query('INSERT INTO projects(name,is_open,team_limit) VALUES(?,?,?)',
                                    (project.name, status, project.limit))
    except IntegrityError:
        return BadRequest(content=f'Project {project.name} already exists')

    project.id = generated_id

    return project


def update(project_update: ProjectUpdate, project: Project):
    try:
        status = Status.from_string(project_update.status)
        status = status.value[0]
    except ValueError:
        return BadRequest(content=f"Project's status {project_update.status} is not valid")

    result = update_query('UPDATE projects SET is_open = ? WHERE id = ?', (status, project.id))

    if result:
        project.status = project_update.status
        return project


def remove_developer_from_project(project: ProjectDB, developer_id: int):
    updated_devs = list(set(project.developers).difference([developer_id]))
    insert_query('DELETE FROM devs_projects WHERE project_id = ? and dev_id =?', (project.id, developer_id))
    project.developers = updated_devs
    return project


def assign_developer_to_project(project: ProjectDB, developer_id: int):
    updated_devs = project.developers
    updated_devs.append(developer_id)
    insert_query('INSERT INTO devs_projects VALUES(?,?)', (developer_id, project.id))
    project.developers = updated_devs
    return project
