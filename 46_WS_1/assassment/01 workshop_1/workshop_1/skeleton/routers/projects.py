from fastapi import APIRouter, Response
from pydantic import BaseModel
from data.models import Projects
from services import projects_services

projects_router = APIRouter(prefix='/projects')


@projects_router.get('/{id}')
def get_project_by_id(id: int):
    project = projects_services.get_by_id(id)

    if project is None:
        return Response(status_code=400)
    
    return project