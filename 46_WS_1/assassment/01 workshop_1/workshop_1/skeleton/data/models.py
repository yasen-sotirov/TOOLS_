from pydantic import BaseModel


class Devs(BaseModel):
    id: int | None = None
    name: str
    level: int

    @classmethod
    def from_query_result(cls, id, name, level):
        return cls(
            id=id,
            name=name,
            level=level)

class Projects(BaseModel):
    id: int | None = None
    name: str
    is_open: int
    team_limit: int

    @classmethod
    def from_query_result(cls, id, name, is_open, team_limit):
        return cls(
            id=id,
            name=name,
            is_open=is_open,
            team_limit=team_limit)