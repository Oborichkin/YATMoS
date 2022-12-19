from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from yatmos.database import Base
from yatmos.common.enums import Status


class Suite(Base):
    __tablename__ = "suites"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    desc = Column(String)
    parent_id = Column(Integer, ForeignKey("suites.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="suites", uselist=False)
    parent = relationship("Suite", remote_side=id, backref="children", uselist=False)
    results = relationship("SuiteResult", back_populates="suite")

    def make_result(self, db, run_id):
        res = SuiteResult(suite_id=self.id, run_id=run_id)
        db.add(res)
        db.commit()
        db.refresh(res)

        for case in self.cases:
            case.make_result(db=db, run_id=run_id, suite_id=res.id)


class SuiteResult(Base):
    __tablename__ = "suite_results"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    status = Column(Enum(Status), default=Status.UNKNOWN)
    suite_id = Column(Integer, ForeignKey("suites.id"))
    run_id = Column(Integer, ForeignKey("runs.id"))

    suite = relationship("Suite", back_populates="results")
    run = relationship("Run", back_populates="suites")
    cases = relationship("CaseResult", back_populates="suite")
