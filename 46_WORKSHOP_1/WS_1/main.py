from fastapi import FastAPI
from data.database import init_database
from routers.developers_router import developer_routers
from routers.projects_router import project_router
import uvicorn

init_database()

app = FastAPI(title="Workshop 1", description="The first workshop in WEB module")
app.include_router(developer_routers)
app.include_router(project_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)


""" TEST LINKS

1. **Get all projects** - returns id, name, status, limit for all projects
    http://127.0.0.1:8000/docs#/default/get_all_projects_1_projects__get
    
    
2. **Get all devs** - returns id, name, level for all devs
    http://127.0.0.1:8000/docs#/default/get_all_dev_2_developers__get
    

3. **Get project by id**
    - returns id, name, status, limit for the project with provided ID
        - returns id, name, level for devs assigned to that project
    http://127.0.0.1:8000/docs#/default/get_project_by_id_3_projects__id__get


4. **Get dev by id**
    - returns id, name, level for the dev with provided ID
        - returns id, name, status, limit for projects assigned to that dev
    http://127.0.0.1:8000/docs#/default/get_dev_by_id_4_developers__id__get


5. **Create project** - required data:
    - name: str - at least one symbol, unique
    - status: str - one of open|closed (note that value should be stored as int in db)
    - limit: int - positive integer
    http://127.0.0.1:8000/docs#/default/create_project_5_projects__post
    {"id": 0, "name": "New project", "is_open": "open", "team_limit": 10}


6. **Create dev** - required data:
    - name: str - at least one symbol, unique
    - level: str - one of junior|mid|senior (note that value should be stored as int in db)
    http://127.0.0.1:8000/docs#/default/create_dev_6_developers__post
    {"id": 0, "name": "Maria", "level": "mid"}


7. **Set project status**
    - sets a project status to open or closed
    http://127.0.0.1:8000/docs#/default/update_project_status_by_id_7_projects__id__put


8. **Assign dev to project**
    - Cannot assign if project is in closed status.
    - Cannot assign if project limit is reached.
    - Only senior devs can be assigned to more than one project.
    - Each project should have at least one senior.
    (не сотана време за това)


9. **Remove dev from project**
    - Do not check experience level when removing.
    http://127.0.0.1:8000/docs#/default/remove_dev_from_project_by_id_9_developers__project_id__dev_id__delete
"""


