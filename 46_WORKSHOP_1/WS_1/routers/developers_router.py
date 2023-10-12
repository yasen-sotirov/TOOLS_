from fastapi import APIRouter, HTTPException
from data.database import read_query, insert_query, update_query, query_count
from data.models import Developer
from routers.projects_router import get_project_by_id_3

DEV_LEVEL = {"junior": 1, "mid": 2, "senior": 3}
LEVEL_DEV = {1: "junior", 2: "mid", 3: "senior"}

developer_routers = APIRouter(prefix='/developers')


"2. Get all devs"
@developer_routers.get('/')
def get_all_dev_2(
        name: str | None=None,
        level: int | None=None):

    if name:
        data = read_query('''SELECT * FROM devs 
                    WHERE name LIKE ?''', (f'%{name}%',))
    elif level:
        data = read_query('''SELECT * FROM devs
                    WHERE level = ?''', (level,))
    else:
        data = read_query('SELECT * FROM devs')

    date_result = data
    return (Developer.dev_from_query_result(*row) for row in date_result)



"4. Get dev by id"
@developer_routers.get('/{id}')
def get_dev_by_id_4(dev_id: int):
    dev_result = read_query('SELECT * FROM devs WHERE id = ?',
                            (dev_id,))
    if not dev_result:
        return {"message": f"Developer with id {id} not found"}

    project_result = read_query('''SELECT * FROM projects
                    INNER JOIN devs_projects ON projects.id = devs_projects.project_id
                    WHERE devs_projects.dev_id = ?''', (dev_id,))
    if not project_result:
        return {"message": "No projects assigned"}

    dev_id, dev_name, dev_level = dev_result[0]
    dev_l = LEVEL_DEV[dev_level]

    dev_info = {"id": dev_id, "name": dev_name, "level": dev_l,
                "projects": [{"id": p[0], "name": p[1], "is open": p[2], "limit": p[3]}
                             for p in project_result],}
    return dev_info



"6. Create dev"
@developer_routers.post('/')
def create_dev_6(dev: Developer):
    if dev.level not in DEV_LEVEL:
        raise HTTPException(status_code=400, detail="Invalid level")

    dev.level = DEV_LEVEL[dev.level]
    insert_query('INSERT INTO devs(name,level) VALUES(?,?)',
        (dev.name, dev.level))

    return {"message": f"Developer {dev.name} assigned successfully"}



"9. Remove dev from project"
@developer_routers.delete('/{project_id}{dev_id}')
def remove_dev_from_project_by_id_9(project_id: int, dev_id:int):
    count = query_count('''SELECT COUNT(*) FROM devs_projects WHERE dev_id = ?''',
                        (dev_id,))
    if count > 0:
        deleted = update_query('''DELETE FROM devs_projects 
                                WHERE dev_id = ? AND project_id = ?''',
                               (dev_id, project_id))
        if deleted:
            return {f"Dev with id {dev_id} was removed from project wit id {project_id}."}

    return {f"Dev with id {dev_id} is not assigned to this project"}




