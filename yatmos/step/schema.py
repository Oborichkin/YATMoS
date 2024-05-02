from typing import Optional

from pydantic import BaseModel

from yatmos.common.enums import Status


class StepBase(BaseModel):
    title: str
    desc: Optional[str] = None


class StepCreate(StepBase):
    pass


class StepUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None


class Step(StepBase):
    id: int
    case_id: int

    model_config = {
        "from_attributes": True
    }


class StepResultBase(BaseModel):
    step_id: int
    case_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str] = None

    model_config = {
        "use_enum_values": True
    }

class StepResult(StepResultBase):
    id: int

    model_config = {
        "from_attributes": True,
        # Надо ли это дублировать если уже определено в StepResultBase?
        "use_enum_values": True
    }