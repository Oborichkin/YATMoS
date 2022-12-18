from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from yatmos.database import Base
from yatmos.common.enums import Status


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    desc = Column(String)
    suite_id = Column(Integer, ForeignKey("suites.id"))

    suite = relationship("Suite", backref="cases")
    steps = relationship("Step", order_by="Step.position", collection_class=ordering_list("position"))
    results = relationship("CaseResult", back_populates="case")

    def make_result(self, db, run_id, suite_id):
        res = CaseResult(run_id=run_id, suite_id=suite_id, case_id=self.id)
        db.add(res)
        db.commit()
        db.refresh(res)

        for step in self.steps:
            step.make_result(db=db, case_id=res.id)


class CaseResult(Base):
    __tablename__ = "case_results"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    status = Column(Enum(Status), default=Status.UNKNOWN)
    case_id = Column(Integer, ForeignKey("cases.id"))
    suite_id = Column(Integer, ForeignKey("suite_results.id"))
    run_id = Column(Integer, ForeignKey("runs.id"))

    case = relationship("Case", back_populates="results")
    run = relationship("Run", back_populates="cases")
    suite = relationship("SuiteResult", back_populates="cases")
    steps = relationship("StepResult", back_populates="case")
