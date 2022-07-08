from typing import Optional

from pydantic import BaseModel


class TestStepBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestStepCreate(TestStepBase):
    pass


class TestStepUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class TestStep(TestStepBase):
    id: int
    case_id: int

    class Config:
        orm_mode = True
