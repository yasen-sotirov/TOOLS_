from fastapi import APIRouter
from pydantic import BaseModel

from common.responses import BadRequest, NotFound, InternalServerError
from data.models import Status, Project, Developer, ProjectUpdate, Level
from services import project_service, developer_service


class ProjectResponseModel(BaseModel):
    project: Project
    developers: list[Developer]


projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(search_name: str | None = None,
                 search_limit: int | None = None,
                 search_status: str | None = None):
    filters = {}
    if search_name:
        filters['name'] = search_name
    if search_limit is not None:
        filters['team_limit'] = search_limit
    if search_status:
        try:
            status = Status.from_string(search_status)
            filters['is_open'] = status.value[0]
        except ValueError:
            return BadRequest(content=f'Search criteria {search_status} is not valid')

    return project_service.all(filters)


@projects_router.get('/{id}')
def get_projects_by_id(id: int):
    project = project_service.get_by_id(id, db=True)

    if project is None:
        return NotFound()
    else:
        return ProjectResponseModel(project=project,
                                    developers=[developer_service.get_by_id(did) for did in project.developers])


@projects_router.post('/', status_code=201)
def create_project(project: Project):
    return project_service.create(project)


@projects_router.put('/{id}')
def update_project(id: int, data: ProjectUpdate):
    project = project_service.get_by_id(id)
    if project is None:
        return NotFound()

    return project_service.update(data, project) or InternalServerError()


@projects_router.delete('/{project_id}/developers/{developer_id}')
def remove_developer(project_id: int, developer_id: int):
    project = project_service.get_by_id(project_id, db=True)
    if project is None:
        return NotFound()

    updated_project = project_service.remove_developer_from_project(project, developer_id)
    return ProjectResponseModel(project=updated_project,
                                developers=[developer_service.get_by_id(did) for did in project.developers])


@projects_router.put('/{project_id}/developers/{developer_id}')
def assign_developer(project_id: int, developer_id: int):
    project = project_service.get_by_id(project_id, db=True)
    developer = developer_service.get_by_id(developer_id)
    if project is None:
        return NotFound(f"Project {project_id} not found")

    if developer is None:
        return NotFound(f"Developer {developer_id} not found")

    if project.status == str(Status.CLOSED):
        return BadRequest(content=f'Project is {str(Status.CLOSED)}')

    if developer_id in project.developers:
        return BadRequest(content=f'Developer {developer.name} already assigned to this project')

    if len(project.developers) == project.limit:
        return BadRequest(content='Project limit is reached')

    if len(developer.projects) and developer.level != str(Level.SENIOR):
        return BadRequest(
            content=f"Developer {developer.name} is not {str(Level.SENIOR)} and cannot be assigned to more than one projects")

    if len(project.developers) + 1 == project.limit:
        seniors = [d for d in [developer_service.get_by_id(did) for did in project.developers]
                   if d.level == str(Level.SENIOR)]
        if not len(seniors) and developer.level != str(Level.SENIOR):
            return BadRequest(
                content=f"Developer {developer.name} is not {str(Level.SENIOR)} and cannot be assigned to this project."
                        f"\nEach project should have at least one senior")

    result = project_service.assign_developer_to_project(project, developer_id)
    if result:
        return ProjectResponseModel(project=result,
                                    developers=[developer_service.get_by_id(did) for did in project.developers])
    return InternalServerError()
