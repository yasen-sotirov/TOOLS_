from fastapi import APIRouter, Response
from services import profiles_ser



profiles_router = APIRouter(prefix='/profiles')


"01. Get all profiles"
@profiles_router.get('/')
def get_all_profiles(country_code: str | None=None):

    result = profiles_ser.all_profiles(country_code)
    return result



"02. Get profile by id"
@profiles_router.get('/{id}')
def get_profiles_by_id(id: int):
    profile_data = profiles_ser.get_by_id(id)

    return profile_data or Response(status_code=404)



"02. Get all country codes"
@profiles_router.get('/codes')
def get_unique_country_codes():
    result = profiles_ser.unique_country_codes()
    return result


















