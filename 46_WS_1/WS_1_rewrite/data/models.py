from pydantic import BaseModel, constr, conint


"МОДЕЛ ПРОЕКТ"
class Project(BaseModel):
    id: int | None = None
    name: constr(min_length=1)      # (^) започва с.  ($) няма нищо след
    status: constr(pattern="^open | closed$")    # (ge=) = greater or equal
    limit: conint(ge=1)
    devs: list = []

    @classmethod
    def from_query_result(cls, id, name, is_open, team_limit, devs=None):
        return cls(id = id,
                   name = name,
                   status = 'open' if is_open else 'closed',
                   limit = team_limit,
                   devs = devs or [])


"МОДЕЛ DEV"
DEV_LEVEL = {1: 'junior', 2: 'mid', 3: 'senior',
             'junior': 1, 'mid': 2, 'senior': 3}

class Dev(BaseModel):
    id: int | None = None
    name: constr(min_length=1)
    level: constr(pattern='^junior | mid | senior$')
    projects: list = []

    @classmethod
    # обръща query резултат в FastApi class
    def from_query_result(cls, id, name, level, projects=None):
        return cls(id = id,
                   name = name,
                   level = DEV_LEVEL[level],
                   projects = projects or [])








