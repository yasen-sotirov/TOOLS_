from fastapi import FastAPI
from data.database import init_database
from routers.devs import devs_router
import uvicorn

init_database()

app = FastAPI()
app.include_router(devs_router)
