from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session

from yatmos.database import Base
from yatmos.run.model import Run
from yatmos.suite.model import Suite
from yatmos.suite.crud import create_suite
from yatmos.suite.schema import SuiteCreate


class Project(Base):
    __tablename__ = "projects"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    title: Column[str] = Column(String, unique=True, index=True)
    desc: Column[str] = Column(String)

    suites = relationship("Suite", lazy="dynamic", back_populates="project")
    runs = relationship("Run", back_populates="project")

    def get_suite(self, db, suite_title, or_create=False):
        if suite := self.suites.filter(Suite.title == suite_title).first():
            return suite
        elif or_create:
            return create_suite(db, SuiteCreate(title=suite_title), self.id)

    def make_run(self, db: Session, title: str, desc: Optional[str] = None, make_suites=True):
        run = Run(title=title, project_id=self.id, desc=desc)
        db.add(run)
        db.commit()
        db.refresh(run)

        if make_suites:
            for suite in self.suites:
                suite.make_result(db=db, run_id=run.id)

        return run
