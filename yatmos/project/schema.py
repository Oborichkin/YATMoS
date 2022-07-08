from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    desc: Optional[str] = None

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend tests"}}


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    title: Optional[str]
    desc: Optional[str]

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend API tests"}}


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
