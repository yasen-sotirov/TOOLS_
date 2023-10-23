from fastapi import APIRouter
from pydantic import BaseModel
from services import profiles_ser



profiles_router = APIRouter(prefix='/profiles')


"1. Get all profiles"
@profiles_router.get('/')
def get_all_profiles(
        country_code: str | None=None):

    result = profiles_ser.all_profiles(country_code)
    return result

























