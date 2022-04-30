from typing import Optional, List

from pydantic import BaseModel


class TestCaseBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestCaseCreate(TestCaseBase):
    pass


class TestCaseUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class TestCase(TestCaseBase):
    id: int
    suite_id: int

    class Config:
        orm_mode = True


class TestSuiteBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestSuiteCreate(TestSuiteBase):
    pass


class TestSuiteUpdate(BaseModel):
    title: Optional[str]
    desc: Optional[str]


class TestSuite(TestSuiteBase):
    id: int
    parent_id: Optional[int]
    project_id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    title: str
    desc: Optional[str] = None

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend tests"}}


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    title: Optional[str]
    desc: Optional[str]

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend API tests"}}


class Project(ProjectBase):
    id: int
    test_suites: List[TestSuite] = []

    class Config:
        orm_mode = True
