from typing import Optional, List

from pydantic import BaseModel


class RunBase(BaseModel):
    title: str
    desc: Optional[str] = None


class RunCreate(RunBase):
    include_suites: List[int] = []
    exclude_suites: List[int] = []
    include_tests: List[int] = []
    exclude_tests: List[int] = []


class RunUpdate(RunBase):
    title: Optional[str]
    desc: Optional[str]


class Run(RunBase):
    id: int
    project_id: int
    

    class Config:
        orm_mode = True
