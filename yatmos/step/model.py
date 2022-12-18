from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship

from yatmos.common.enums import Status
from ..database import Base


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(Integer)
    title = Column(String, unique=True)
    desc = Column(String)
    case_id = Column(Integer, ForeignKey("cases.id"))

    results = relationship("StepResult", back_populates="step")

    def make_result(self, db, case_id):
        res = StepResult(step_id=self.id, case_id=case_id)
        db.add(res)
        db.commit()
        db.refresh(res)


class StepResult(Base):
    __tablename__ = "step_results"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    status = Column(Enum(Status), default=Status.UNKNOWN)
    step_id = Column(Integer, ForeignKey("steps.id"))
    case_id = Column(Integer, ForeignKey("case_results.id"))

    step = relationship("Step", back_populates="results")
    case = relationship("CaseResult", back_populates="steps")
