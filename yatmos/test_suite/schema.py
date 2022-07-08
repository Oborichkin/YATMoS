from typing import Optional

from pydantic import BaseModel


class TestSuiteBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestSuiteCreate(TestSuiteBase):
    pass


class TestSuiteUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class TestSuite(TestSuiteBase):
    id: int
    parent_id: Optional[int]
    project_id: int

    class Config:
        orm_mode = True
