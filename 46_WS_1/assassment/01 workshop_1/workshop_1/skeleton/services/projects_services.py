from data.models import Projects
from data.database import insert_query, read_query, update_query, init_database

def get_by_id(id: int):
    
    data = read_query(
    '''SELECT p.id AS project_id, p.name AS project_name, p.is_open AS project_status, p.team_limit AS project_limit
       FROM projects AS p
       LEFT JOIN projects AS p ON dp.project_id = p.id
       WHERE p.id = ?''', (id,))

    project = None
    projects = []

    for row in data:
        if project is None:
            project = {
                "id": row[0],
                "name": row[1],
                "is_open": row[2],
                "team_limit": row[3]
            }
            projects.append(project)
        return project

    return None