from data.database import read_query
from data.models import Project



def project_by_id(id: int):
    all_projects = read_query('SELECT * FROM projects')

    for el in all_projects:
        if el[0] == id:
            return Project(id=id, name=el[1], is_open=el[2],team_limit=el[3])
    return {"message": f"Project with {id} not found"}

