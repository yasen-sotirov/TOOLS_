from pydantic import BaseModel, constr
from typing import Union

class Developer(BaseModel):
    id: int
    name: constr(min_length=1)
    level: Union[int, str]

    @classmethod
    def dev_from_query_result(cls, id, name, level):
        if level == 1:
            level = "junior"
        elif level == 2:
            level = "mid"
        else:
            level = "senior"
        return cls(id=id, name=name, level=level)



class Project(BaseModel):
    id: int
    name: constr(min_length=1)
    is_open: Union[int, str]
    team_limit: int

    @classmethod
    def projects_from_query_result(cls, id, name, is_open, team_limit):
        if is_open == 0:
            is_open = "closed"
        else:
            is_open = "open"
        return cls(id=id, name=name, is_open=is_open, team_limit=team_limit)



