from fastapi import APIRouter, Response
from services import projects_service, developers_service
from data.models import Project, ProjectUpdate, Developer


projects_router = APIRouter(prefix='/projects')


@projects_router.get('/')
def get_projects(
    name: str | None = None,
    limit: int | None = None,
    status: str | None = None
):
    return projects_service.get_all(name, limit, status)


@projects_router.get('/{id}')
def get_project_by_id(id: int):
    project = projects_service.get_by_id_with_devs(id)

    return project or Response(status_code=404)


@projects_router.post('/')
def create_project(project: Project):
    project = projects_service.create(project)

    return projects_service.create_response_object(project, [])


@projects_router.put('/{id}')
def update_project_status(id: int, data: ProjectUpdate):
    project = projects_service.update(id, data)

    return {'result': f'{project} updated status'}


@projects_router.put('/{project_id}/{dev_id}')
def assign_devs_to_project(project_id: int, dev_id: int):
    
    project = projects_service.get_by_id(project_id)
    p_developers = projects_service.get_devs_for_project(project)
    developer = developers_service.get_by_id(dev_id)
    d_projects = developers_service.get_projects_for_dev(developer)

    if project.status == 'closed':
        return Response(status_code=400, content="Cannot assign to a project with status closed")   

    if len(p_developers) == project.limit:
        return Response(status_code=400, content='Reached limit for assignment')

    if not developer.level == 'senior' and len(d_projects) == 1:
        return Response(status_code=400, content='Only senior developers can have more than one project') 

    if not developer.level == 'senior' and len(p_developers) == (project.limit - 1):
            return Response(status_code=400, content='Must have at least one senior in the project')

    success = projects_service.assign_dev_to_project(project, developer)

    if success:
        return {
            "message": f"Developer {developer.id} assigned to Project {project.id} successfully"
        }
    else:
        return Response(status_code=400, content='Failed to assign developer to project')


@projects_router.delete('/remove_dev/{project_id}/{dev_id}')
def remove_dev_from_project(project_id: int, dev_id: int):
    success = projects_service.remove_dev_from_project(project_id, dev_id)
    
    if success:
        return {"message": f"Developer with id: {dev_id} removed from project with id: {project_id} successfully"}
    else:
        return Response(status_code=400, content="Failed to remove developer from project")