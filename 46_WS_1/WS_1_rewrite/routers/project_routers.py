from fastapi import APIRouter, Query, Response, Body
from fastapi.responses import JSONResponse
from data.models import Project, Dev, DEV_LEVEL
from data.database import read_query, query_count, insert_query, update_query
from services.project_services import create, project_id_exists
from services.dev_services import dev_id_exists

projects_router = APIRouter(prefix='/projects')


"1. Get all projects "
@projects_router.get
def get_all_projects(name: str | None,
                     limit: int | None,
                     status: str | None = Query(default=None, regex='^open|close$')):

    sql = 'SELECT id, name, is_open, team_limit FROM projects'
    where_clause = []

    if name:
        where_clause.append(f"name like '%{name}%")
    if limit:
        where_clause.append(f"team_limit <= {limit}")
    if status:
        where_clause.append(f"is_open = {1 if status == 'open' else 0}")

    if where_clause:
        sql += ' WHERE ' + ' AND '.join(where_clause)

    return (Project.from_query_result(*row) for row in read_query(sql))




"3. Get project by id"
@projects_router.get('/{id}')
def get_project_by_id(id: int):
    project_data = read_query('''SELECT id, name, is_open, team_limit
                            FROM projects WHERE id = ?''', (id,))
    if project_data is None:
        return None

    dev_data = read_query('''SELECT id, name, level FROM devs
                JOIN devs_project ON id WHERE project_id = ?''',(id,))

    project = Project.from_query_result(
        *project_data[0], [Dev.from_query_result(*row) for row in dev_data])

    return project or Response(status_code=404)


"5. Create project"
# ако създаде успешно връща статус 201
@projects_router.post('/', status_code=201)
def create_project(project: Project):
    name_exists = query_count('SELECT COUNT(*) FROM projects WHERE name = ?',
                              (project.name,))
    if name_exists:
        # 409 сървъра среща конфликт. Например, ако се опитате да създадете
        # ресурс, който вече съществува, код 409 указате, че вече има конфликт със съществуващия ресурс.
        return JSONResponse(status_code=409, content={'detail': 'Project name must be unique'})

    return create(project)



"7. Set project status"
@projects_router.put('/{id}/status')
def change_project_status(id: int,
                status: str = Body(embed=True, regex='^open|closed$')):

    if not project_id_exists(id):
        return Response(status_code=404)

    update_query('UPDATE projects SET is_open = ? WHERE id = ?',
                        (1 if status=='open' else 0, id))

    return {'message': f'Status set to {status}.'}


"8. Assign dev to project"
@projects_router.post('/{project_id}/devs/{dev_id}')
# при POST заявка към /projects/123/devs/456,
# FastAPI ще извади стойностите 123 и 456 за project_id и dev_id
# от URL-а и ще ги предаде на съответната функция за обработка.
def assign_dev_to_project(project_id: int, dev_id: int):
    # съществува ли такъв проект
    if not project_id_exists(project_id):
        return JSONResponse(status_code=404,
                            content={'detail': f'No project with id {project_id}'})

    # съществува ли такъв dev
    if not dev_id_exists(dev_id):
        return JSONResponse(status_code=404,
                            content={'detail': f'No dev with id {dev_id}'})

    # дали този dev вече не работи по този проект
    if query_count('SELECT COUNT(*) FROM devs_projects '
                    'WHERE dev_id - ? AND project_id = ?',
                   (dev_id, project_id)) > 0:
        return False, 'Dev already assigned to project.'

    # проверява статуса на проекта
    limit, is_open = read_query('SELECT team_limit, is_open '
                                'FROM projects WHERE id = ?',
                                (project_id,))[0]
    if not is_open:
        return False, 'Cannot assign to closed projects.'

    # проверява team_limit на проекта
    project_dev_levels = read_query('SELECT level FROM devs '
                                    'JOIN devs_projects ON id = dev_id '
                                    'WHERE project_id = ?', (project_id,))
    devs_counter = len(project_dev_levels)
    if limit == devs_counter:
        return False, 'Cannot assign additional devs to full projects.'


    dev_level, dev_projects_count = read_query(
        'SELECT level, (SELECT COUNT(*) FROM devs_projects WHERE dev_id = id) '
        'FROM devs WHERE id = ?', (dev_id,))[0]
    senior_level = DEV_LEVEL["senior"]
    has_no_senior = all(level[0] < senior_level for level in project_dev_levels)

    # проектът има ли поне един старши
    if has_no_senior and (devs_counter + 1 ==limit) and (dev_level < senior_level):
        return False, 'At least one senior must be assigned to a project.'

    # може ли да бъде назначен на още проекти
    if dev_projects_count > 0 and dev_level < senior_level:
        return False, 'Only senior devs can be assigned to more than one project.'

    insert_dev = insert_query('INSERT INTO devs_projects(dev_id, project_id)'
                 'VALUES (?,?)', (dev_id, project_id))

    description = 'Dev assigned to project.'

    return JSONResponse(
        status_code=200 if insert_dev else 409,
        content={'message' if insert_dev else 'detail': description})



"9. Remove dev from project"
@projects_router.delete('/{project_id}/devs/{dev_id}')
def remove_dev_from_project(project_id: int, dev_id: int):
    # съществува ли този проект
    if not project_id_exists(project_id):
        return JSONResponse(status_code=404,
                            content={'detail': f'No project with id {project_id}'})

    # съществува ли този dev
    if not dev_id_exists(dev_id):
        return JSONResponse(status_code=404,
                            content={'detail': f'No dev with id {dev_id}'})

    # този dev назначен ли е на този проект
    if query_count('''SELECT COUNT(*) FROM devs_projects 
                   WHERE dev_id = ? AND project_id = ?''', (dev_id, project_id)) == 0:
        return JSONResponse(status_code=404, content='Dev not assigned to this project.')

    # премахва
    update_query('''DELETE FROM devs_projects 
                    WHERE dev_id = ? AND project_id = ?''',
                 (dev_id, project_id))
    return JSONResponse(status_code=200, content='Dev removed from project.')





