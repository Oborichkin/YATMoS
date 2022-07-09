from typing import Optional

from pydantic import BaseModel


class TestRunBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestRunCreate(TestRunBase):
    pass


class TestRunUpdate(TestRunBase):
    title: Optional[str]
    desc: Optional[str]


class TestRun(TestRunBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True
