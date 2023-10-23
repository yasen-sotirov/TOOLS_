from pydantic import BaseModel


class Developer(BaseModel):
    id: int | None
    name: str
    level: str

    @classmethod
    def from_query_result(cls, id, name, level):
        level_mapping = {1:'junior', 2:'mid', 3:'senior'}
        if level in level_mapping:
            level = level_mapping[level]
        return cls(
            id=id,
            name=name,
            level=level)


class DeveloperCreate(BaseModel):
    id: int | None    
    name: str
    level: int


class Project(BaseModel):
    id: int | None
    name: str
    status: str
    limit: int

    @classmethod
    def from_query_result(cls, id, name, status, limit):
        status_mapping = {1:'open', 0:'closed'}
        if status in status_mapping:
            status = status_mapping[status]
        return cls(
            id=id,
            name=name,
            status=status,
            limit=limit)
    

class ProjectUpdate(BaseModel):
    status: str

