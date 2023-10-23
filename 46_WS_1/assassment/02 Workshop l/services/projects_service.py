from data.database import read_query, insert_query, update_query, query_count
from data.models import Project, Developer, ProjectUpdate

status_mapping = {'open': 1, 'closed': 0}


def get_all(name: str = None, status: str = None, limit: int = None):
    stat = status_mapping.get(status)
    base_query = "SELECT * FROM projects WHERE 1=1"
    query_params = []

    if name:
        base_query += " AND name LIKE ?"
        query_params.append(f'%{name}%')

    if limit is not None:
        base_query += " AND team_limit = ?"
        query_params.append(limit)

    if stat is not None:
        base_query += " AND is_open = ?"
        query_params.append(stat)

    data = read_query(base_query, tuple(query_params))
    return (Project.from_query_result(*row) for row in data)


def get_by_id_with_devs(id: int):
    project = get_by_id(id)

    if project is None:
        return None

    developers_data = get_devs_for_project(project)

    return create_response_object(
        project,
        [Developer.from_query_result(*dev) for dev in developers_data])


def get_by_id(id: int):
    project_data = read_query(
        '''SELECT * FROM projects WHERE id = ?''', (id,))

    return next((Project.from_query_result(*row) for row in project_data), None)


def get_devs_for_project(project: Project):
    developers_data = read_query(
        """SELECT d.id, d.name, d.level FROM devs d
           WHERE d.id IN (SELECT dev_id FROM devs_projects WHERE project_id = ?)""",
        (project.id,))

    return developers_data


def create(project: Project):
    generated_id = insert_query(
        '''INSERT INTO projects(name, is_open, team_limit) VALUES(?, ?, ?)''',
        (project.name, project.status, project.limit))

    project.id = generated_id
    return project


def update(project_id: int, project: ProjectUpdate):
    status = status_mapping.get(project.status.lower())

    if status is None:
        raise ValueError("Invalid project status")

    result = update_query(
        '''UPDATE projects SET is_open = ? WHERE id = ?''',
        (status, project_id))

    return result


def assign_dev_to_project(project: Project, developer: Developer) -> bool:
    try:
        return update_query(
            """INSERT INTO devs_projects(dev_id, project_id) VALUES(?, ?)""",
            (developer.id, project.id))

    except Exception as e:
        print(f'Error assigning developer to project: {str(e)}')
        return False


def remove_dev_from_project(project_id: int, dev_id: int) -> bool:
    try:
        return update_query(
            'DELETE FROM devs_projects WHERE project_id = ? AND dev_id = ?',
            (project_id, dev_id))

    except Exception as e:
        print(f"Error removing developer from project: {str(e)}")
        return False


def create_response_object(project: Project, devs: list[Developer]):
    return {
        'id': project.id,
        'name': project.name,
        'status': project.status,
        'team_limit': project.limit,
        'developers': devs
    }
