from typing import Optional

from pydantic import BaseModel


class RunBase(BaseModel):
    title: str
    desc: Optional[str] = None


class RunCreate(RunBase):
    pass


class RunUpdate(RunBase):
    title: Optional[str] = None
    desc: Optional[str] = None


class Run(RunBase):
    id: int
    project_id: int

    model_config = {
        "from_attributes": True
    }
