from typing import Optional

from pydantic import BaseModel

from yatmos.common.enums import Status


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


class StepResultBase(BaseModel):
    step_id: int
    case_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str]

    class Config:
        use_enum_values = True


class StepResult(StepResultBase):
    id: int

    class Config(StepResultBase.Config):
        orm_mode = True
