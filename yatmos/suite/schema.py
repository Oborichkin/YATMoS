from typing import Optional

from pydantic import BaseModel

from yatmos.common.enums import Status


class SuiteBase(BaseModel):
    title: str
    desc: Optional[str] = None


class SuiteCreate(SuiteBase):
    pass


class SuiteUpdate(BaseModel):
    title: Optional[str] = None
    desc: Optional[str] = None


class Suite(SuiteBase):
    id: int
    parent_id: Optional[int] = None
    project_id: int

    model_config = {
        "from_attributes": True
    }


class SuiteResultBase(BaseModel):
    suite_id: int
    run_id: int
    status: Status = Status.UNKNOWN
    comment: Optional[str] = None

    model_config = {
        "use_enum_values": True
    }


class SuiteResultUpdate(BaseModel):
    status: Optional[Status] = None
    comment: Optional[str] = None


class SuiteResult(SuiteResultBase):
    id: int

    model_config = {
        "from_attributes": True,
        # Надо ли это дублировать если в родительском классе уже указано?
        "use_enum_values": True,
    }

