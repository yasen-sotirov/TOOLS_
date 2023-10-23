from fastapi import APIRouter
from services import profiles_ser



profiles_router = APIRouter(prefix='/profiles')


"01. Get all profiles"
@profiles_router.get('/')
def get_all_profiles(
        country_code: str | None=None):

    result = profiles_ser.all_profiles(country_code)
    return result



"02. Get profile by id"
@profiles_router.get('/{id}')
def get_profiles_by_id(id: int):
    project = profiles_ser.get_by_id(id)

    return project or Response(status_code=404)





















