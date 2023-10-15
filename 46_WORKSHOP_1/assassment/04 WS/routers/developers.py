from fastapi import APIRouter
from common.responses import NotFound
from data.models import Developer
from services import developer_service, project_service
from services.developer_service import create_response

devs_router = APIRouter(prefix='/developers')


@devs_router.get('/')
def get_developers(search: str = None, searchlevel: str = None):
    return developer_service.all(search, searchlevel)


@devs_router.get('/{id}')
def get_dev_by_id(id: int):
    dev = developer_service.get_dev_by_id(id)
    if dev:
        projects = project_service.get_projects_by_dev(id)
        return create_response(dev, projects)
    return NotFound('The searched developer does not exist in the database!')


@devs_router.post('/')
def create_dev(dev: Developer):
    return developer_service.create_dev(dev)



