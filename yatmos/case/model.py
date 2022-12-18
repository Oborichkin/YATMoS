from sqlalchemy import Column, String, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from yatmos.database import Base
from yatmos.step.model import Step  # FIXME: Remove this line
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

    def make_result(self, suite_result_id):
        return CaseResult(case_id=self.id, suite_id=suite_result_id)


class CaseResult(Base):
    __tablename__ = "case_results"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    status = Column(Enum(Status), default=Status.UNKNOWN)
    case_id = Column(Integer, ForeignKey("cases.id"))
    suite_id = Column(Integer, ForeignKey("suite_results.id"))

    case = relationship("Case", back_populates="results")
    suite = relationship("SuiteResult", back_populates="cases")
