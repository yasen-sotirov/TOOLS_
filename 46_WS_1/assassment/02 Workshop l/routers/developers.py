from fastapi import APIRouter, Response
from services import developers_service
from data.models import DeveloperCreate

developers_router = APIRouter(prefix='/developers')


@developers_router.get('/')
def get_developers(
        name: str | None = None,
        level: str | None = None
):
    result = developers_service.get_all(name, level)
    if not result:
        return Response(status_code=404, content='NOT FOUND')
    else:
        return result


@developers_router.get('/{id}')
def get_developer_by_id(id: int):
    developer = developers_service.get_by_id_with_projects(id)

    return developer or Response(status_code=404)


@developers_router.post('/')
def create_developer(developer: DeveloperCreate):
    developer = developers_service.create(developer)

    return developers_service.create_response_object(developer, [])
