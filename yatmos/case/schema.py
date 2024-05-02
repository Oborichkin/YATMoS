from typing import Optional

from pydantic import BaseModel

from yatmos.common.enums import Status


class CaseBase(BaseModel):
    title: str
    desc: Optional[str] = None


class CaseCreate(CaseBase):
    pass


class CaseUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None


class Case(CaseBase):
    id: int
    suite_id: int

    model_config = {
        "from_attributes": True
    }


class CaseResultBase(BaseModel):
    case_id: int
    suite_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str] = None

    model_config = {
        "use_enum_values": True
    }


class CaseResultUpdate(BaseModel):
    status: Optional[Status] = None
    comment: Optional[str] = None


class CaseResult(CaseResultBase):
    id: int

    model_config = {
        "from_attributes": True
    }
