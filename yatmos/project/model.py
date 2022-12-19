from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Session

from yatmos.database import Base
from yatmos.run.model import Run


class Project(Base):
    __tablename__ = "projects"

    id: Column[int] = Column(Integer, primary_key=True, index=True)
    title: Column[str] = Column(String, unique=True, index=True)
    desc: Column[str] = Column(String)

    suites = relationship("Suite", lazy="joined", back_populates="project")
    runs = relationship("Run", back_populates="project")

    def make_run(self, db: Session, title: str, desc: Optional[str] = None):
        run = Run(title=title, project_id=self.id, desc=desc)
        db.add(run)
        db.commit()
        db.refresh(run)

        for suite in self.suites:
            suite.make_result(db=db, run_id=run.id)

        return run
