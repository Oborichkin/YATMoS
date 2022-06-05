from typing import Optional, List

from pydantic import BaseModel


class TestCaseBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestCaseCreate(TestCaseBase):
    pass


class TestCaseUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class TestCase(TestCaseBase):
    id: int
    suite_id: int

    class Config:
        orm_mode = True
