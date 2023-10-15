from fastapi import FastAPI
from data.database import init_database
from routers.developers import developers_router
from routers.projects import projects_router

init_database()

app = FastAPI()
app.include_router(developers_router)
app.include_router(projects_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)