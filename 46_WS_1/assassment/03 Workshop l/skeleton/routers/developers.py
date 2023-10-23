from fastapi import APIRouter
from pydantic import BaseModel

from common.responses import BadRequest, NotFound
from data.models import Level, Developer, Project
from services import developer_service, project_service


class DeveloperResponseModel(BaseModel):
    developer: Developer
    projects: list[Project]


developers_router = APIRouter(prefix='/developers')


@developers_router.get('/')
def get_developers(search_name: str | None = None, search_level: str | None = None):
    filters = {}
    if search_name:
        filters['name'] = search_name
    if search_level:
        try:
            level = Level.from_string(search_level)
            filters['level'] = level.value[0]
        except ValueError:
            return BadRequest(content=f'Search criteria {search_level} is not valid')

    return developer_service.all(filters)


@developers_router.get('/{id}')
def get_developer_by_id(id: int):
    developer = developer_service.get_by_id(id)

    if developer is None:
        return NotFound()
    else:
        return DeveloperResponseModel(developer=developer,
                                      projects=[project_service.get_by_id(pid) for pid in developer.projects])


@developers_router.post('/', status_code=201)
def create_product(developer: Developer):
    return developer_service.create(developer)
