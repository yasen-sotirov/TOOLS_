from data.models import Project
from data.database import insert_query, read_query, query_count, update_query


def create(project: Project):
    generated_id = insert_query(
        'INSERT INTO projects(name,is_open,team_limit) VALUES(?,?,?)',
        (project.name, 1 if project.status == 'open' else 0, project.limit))

    project.id = generated_id

    return project


def project_id_exists(project_id: int):
    return query_count('SELECT COUNT(*) from projects WHERE id = ?',
                       (project_id,)) > 0