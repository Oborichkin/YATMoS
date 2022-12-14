from enum import Enum
from typing import Optional

from pydantic import BaseModel


class SuiteBase(BaseModel):
    title: str
    desc: Optional[str]


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


class Status(str, Enum):
    UNKNOWN = "UNKNOWN"
    PASS = "PASS"
    FAIL = "FAIL"


class SuiteResultBase(BaseModel):
    suite_id: int
    run_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str]

    class Config:
        use_enum_values = True


class SuiteResultUpdate(BaseModel):
    status: Optional[Status]
    comment: Optional[str]


class SuiteResult(SuiteResultBase):
    id: int

    class Config:
        orm_mode = True
        use_enum_values = True
