from fastapi import APIRouter
from common.responses import BadRequest, NotFound, OK, NoContent
from data.database import read_query, insert_query, update_query
from data.models import Project, Status, Developer
from services import project_service, developer_service
from services.developer_service import get_devs_by_project
from services.project_service import create_response

projects_router = APIRouter(prefix='/projects')



@projects_router.get('/')
def get_projects(search: str = None, searchlimit: int = None, searchstatus: str = None):
    return project_service.all(search,searchlimit,searchstatus)


@projects_router.get('/{id}')
def get_project_by_id(id: int):
    project = project_service.get_project_by_id(id)
    if project:
        devs = get_devs_by_project(id)
        return create_response(project, devs)
    return NotFound('The searched project does not exist in the database!')


@projects_router.post('/')
def create_project(project: Project):
    if project.limit <= 0:
        return BadRequest('Team limit must be at least 1 person!')
    return project_service.create_project(project)


@projects_router.patch('/{id}')
def update_project_status(id: int, status: Status):
    return project_service.update_status(id, status)

@projects_router.put('/{id}')
def assign_dev_to_project(id: int, dev_id: int):
    dev = developer_service.get_dev_by_id(dev_id)
    if dev is None:
        return NotFound('The developer is not valid.')
    dev_projects = project_service.get_projects_by_dev(dev.id)
    project = project_service.get_project_by_id(id)
    if project is None:
        return NotFound('The project is not valid.')
    project_devs = developer_service.get_devs_by_project(id)
    if project.status == "closed":
        return BadRequest('The project is closed and cannot assign developers to it.')
    if project.limit == len(project_devs):
        return BadRequest('The project team limit is reached.')
    if not dev.level == 'senior' and dev_projects:
        return BadRequest('The developer is not senior and cannot be assigned to more than one project')
    if 'senior' not in [dev.level for dev in project_devs] and project.limit - len(project_devs) == 1 and not dev.level == 'senior':
        return BadRequest('The project needs senior developer.')
    if dev.id in [dev.id for dev in project_devs]:
        return BadRequest('The developer is already part of the team.u')
    project_service.assign_dev_to_project(id, dev.id)
    return OK('Developer was assigned to project.')


@projects_router.delete('/{id}')
def remove_dev_from_project(id: int, dev_id: int):
    project = project_service.get_project_by_id(id)
    if project is None:
        return NotFound('The project is not valid.')
    project_devs = [dev.id for dev in get_devs_by_project(id)]
    if dev_id not in project_devs:
        return BadRequest('The developer is not part of this project.')
    project_service.delete_def_from_project(id, dev_id)
    return NoContent()






