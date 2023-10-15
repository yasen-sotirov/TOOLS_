from enum import Enum

from pydantic import BaseModel, PositiveInt, constr


class Level(Enum):
    JUNIOR = (1, 'junior')
    MID = (2, 'mid')
    SENIOR = (3, 'senior')

    def __str__(self):
        return self.value[1]

    @classmethod
    def from_string(cls, s):
        for level in cls:
            if level.value[1] == s:
                return level
        raise ValueError(cls.__name__ + ' has no value matching "' + s + '"')

    @classmethod
    def from_integer(cls, i):
        for level in cls:
            if level.value[0] == i:
                return level
        raise ValueError(cls.__name__ + ' has no value matching "' + i + '"')


class Status(Enum):
    OPEN = (1, "open")
    CLOSED = (0, "closed")

    def __str__(self):
        return self.value[1]

    @classmethod
    def from_string(cls, s):
        for status in cls:
            if status.value[1] == s:
                return status
        raise ValueError(cls.__name__ + ' has no value matching "' + s + '"')

    @classmethod
    def from_integer(cls, i):
        for status in cls:
            if status.value[0] == i:
                return status
        raise ValueError(cls.__name__ + ' has no value matching "' + i + '"')


class Developer(BaseModel):
    id: int | None = None
    name: constr(min_length=1)
    level: str

    @classmethod
    def from_query_result(cls, id, name, level):
        level = Level.from_integer(level)
        return cls(
            id=id,
            name=name,
            level=str(level))


class DeveloperDB(Developer):
    projects: list[int] = []

    @classmethod
    def from_query_result(cls, id, name, level, projects=''):
        if projects == '' or projects is None:
            projects = []
        else:
            projects = list(map(int, projects.split(',')))
        level = Level.from_integer(level)
        return cls(
            id=id,
            name=name,
            level=str(level),
            projects=projects)


class Project(BaseModel):
    id: int | None = None
    name: constr(min_length=1)
    status: str
    limit: PositiveInt

    @classmethod
    def from_query_result(cls, id, name, status, limit):
        status = Status.from_integer(status)
        return cls(
            id=id,
            name=name,
            status=str(status),
            limit=limit)


class ProjectDB(Project):
    developers: list[int]

    @classmethod
    def from_query_result(cls, id, name, status, limit, developers=''):
        if developers == '' or developers is None:
            developers = []
        else:
            developers = list(map(int, developers.split(',')))
        status = Status.from_integer(status)
        return cls(
            id=id,
            name=name,
            status=str(status),
            limit=limit,
            developers=developers)


class ProjectUpdate(BaseModel):
    status: str
