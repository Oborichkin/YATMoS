from typing import Optional

from pydantic import BaseModel


class SuiteBase(BaseModel):
    title: str
    desc: Optional[str] = None


class SuiteCreate(SuiteBase):
    pass


class SuiteUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class Suite(SuiteBase):
    id: int
    parent_id: Optional[int]
    project_id: int

    class Config:
        orm_mode = True
