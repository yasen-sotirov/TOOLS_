from fastapi import APIRouter, Response, HTTPException
from pydantic import BaseModel
from data.database import read_query, insert_query, update_query
from data.models import Project, Developer
from services import services


class ProjectResponseModel(BaseModel):
    name: Project
    devs: list[Developer]

PROJECT_STATUS = {"open": 1, "closed": 0}

project_router = APIRouter(prefix='/projects')


"1. Get all projects"
@project_router.get('/')
def get_all_projects_1(
        name: str | None = None,
        is_open: str | None = None,
        team_limit: int | None = None):

    if name:
        data = read_query('''SELECT * FROM projects 
            WHERE name LIKE ?''', (f'%{name}%',))

    elif team_limit:
        data = read_query('''SELECT * FROM projects
            WHERE team_limit <= ?''', (team_limit,))

    elif is_open:
        if is_open == 'open':
            data = read_query('''SELECT * FROM projects
            WHERE is_open = ?''', (1,))
        else:
            data = read_query('''SELECT * FROM projects 
            WHERE is_open = ?''', (0,))
    else:
        data = read_query('SELECT * FROM projects')

    date_result = data
    return (Project.projects_from_query_result(*row) for row in date_result)



"3. Get project by id"
@project_router.get('/{id}')
def get_project_by_id_3(project_id: int):
    project_result = read_query("SELECT * FROM projects WHERE id = ?",
                                (project_id,))
    if not project_result:
        return {"message": f"The project with id {project_id} not found."}

    project_id, project_name, is_open, team_limit = project_result[0]

    devs_result = read_query("""SELECT * FROM devs
                INNER JOIN devs_projects ON devs.id = devs_projects.dev_id
                WHERE devs_projects.project_id = ?""", (project_id,))
    if not devs_result:
        return {"Not assigned devs to this project."}

    STATUS_P = {1: "open", 0: "closed"}
    status = STATUS_P[is_open]
    project_info = {
        "id": project_id,
        "name": project_name,
        "is_open": status,
        "team_limit": team_limit,
        "developers": [{"id": dev[0], "name": dev[1], "level": dev[2]} for dev in devs_result],}
    return project_info



"5. Create project"
@project_router.post('/')
def create_project_5(project: Project):
    if project.team_limit <= 0:
        raise HTTPException(status_code=422, detail="The team limit must be at least 1")

    project.is_open = PROJECT_STATUS[project.is_open]
    insert_query('INSERT INTO projects(name,is_open,team_limit) VALUES(?,?,?)',
                 (project.name, project.is_open, project.team_limit))
    return {"message": f"The project {project.name} was created successfully"}



"7. Set project status"
@project_router.put('/{id}')
def update_project_status_by_id_7(id: int, is_open:str):
    existing_p = services.project_by_id(id)

    if not existing_p:
        return Response(status_code=400,
                        content=f'Project with {id} does not exist')
    else:
        status = PROJECT_STATUS[is_open]

        updated_p = Project(
            id=existing_p.id,
            name = existing_p.name,
            is_open = status,
            team_limit = existing_p.team_limit)

        update_query('''UPDATE projects
            SET name = ?, is_open = ?, team_limit = ? WHERE id = ?''',
            (updated_p.name, updated_p.is_open, updated_p.team_limit, id))

        return {"message": f"The project with id {id} is updated to status '{is_open}'."}

