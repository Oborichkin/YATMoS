from typing import Optional, List

from pydantic import BaseModel


class RunBase(BaseModel):
    title: str
    desc: Optional[str] = None


class RunCreate(RunBase):
    pass


class RunUpdate(RunBase):
    title: Optional[str]
    desc: Optional[str]


class Run(RunBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True
