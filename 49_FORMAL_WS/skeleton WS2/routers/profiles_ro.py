from fastapi import APIRouter
from pydantic import BaseModel
from services import profiles_ser



profile_router = APIRouter(prefix='/profile')


"1. Get all profiles"
@profile_router.get('/')
def get_all_profiles(
        country_code: str | None=None):

    result = profiles_ser.all_profiles(country_code)
    return result

























