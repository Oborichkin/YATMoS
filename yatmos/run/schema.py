from typing import Optional

from typing import List
from pydantic import BaseModel
from yatmos.suite.schema import SuiteResult
from yatmos.case.schema import CaseResult


class RunBase(BaseModel):
    title: str
    desc: Optional[str] = None


class RunCreate(RunBase):
    pass


class RunUpdate(RunBase):
    title: Optional[str] = None
    desc: Optional[str] = None


class Run(RunBase):
    id: int
    project_id: int
    suites: List[SuiteResult]
    cases: List[CaseResult]

    model_config = {
        "from_attributes": True
    }
