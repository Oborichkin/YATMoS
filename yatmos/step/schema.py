from typing import Optional

from pydantic import BaseModel


class StepBase(BaseModel):
    title: str
    desc: Optional[str] = None


class StepCreate(StepBase):
    pass


class StepUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class Step(StepBase):
    id: int
    case_id: int

    class Config:
        orm_mode = True
