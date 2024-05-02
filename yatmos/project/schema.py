from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    desc: Optional[str] = None

    model_config = {
        "json_schema_extra": {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend tests"}}
    }

class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    title: Optional[str] = None
    desc: Optional[str] = None

    model_config = {
        "json_schema_extra": {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend API tests"}}
    }

class Project(ProjectBase):
    id: int

    model_config = {
        "from_attributes": True
    }