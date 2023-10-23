from fastapi import APIRouter, Response
from pydantic import BaseModel
from data.models import Devs
from services import devs_services

devs_router = APIRouter(prefix='/devs')


@devs_router.get('/')
def get_all_devs(
    filter_by_name: str | None = None,
    filter_by_exp: str | None = None,
):
    result = devs_services.all(filter_by_name)

    if filter_by_exp:
        return devs_services.sort(filter_by_exp)
    else:
        return result


@devs_router.get('/{id}')
def get_dev_by_id(id: int):
    dev = devs_services.get_by_id(id)

    if dev is None:
        return Response(status_code=400)
    
    return dev


@devs_router.post('/', status_code=201)
def create_dev(dev: Devs):


    return devs_services.create(dev)