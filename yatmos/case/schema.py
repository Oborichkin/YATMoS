from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class Status(str, Enum):
    UNKNOWN = -1
    PASS = 0
    FAIL = 1


class CaseBase(BaseModel):
    title: str
    desc: Optional[str] = None


class CaseCreate(CaseBase):
    pass


class CaseUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class Case(CaseBase):
    id: int
    suite_id: int

    class Config:
        orm_mode = True


class CaseResultBase(BaseModel):
    case_id: int
    suite_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str]

    class Config:
        use_enum_values = True


class CaseResultUpdate(BaseModel):
    status: Optional[Status]
    comment: Optional[str]


class CaseResult(CaseResultUpdate):
    id: int

    class Config(CaseResultUpdate.Config):
        orm_mode = True
