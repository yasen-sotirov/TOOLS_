from pydantic import BaseModel


class Developer(BaseModel):
    id: int | None = None
    name: str
    level: str


class Project(BaseModel):
    id: int | None = None
    name: str
    status: str
    limit: int


class Status(BaseModel):
    status: str