from typing import Optional, List

from pydantic import BaseModel


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
