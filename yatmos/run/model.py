from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from yatmos.database import Base
from yatmos.suite.model import SuiteResult


class Run(Base):
    __tablename__ = "runs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    desc = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    suites = relationship(SuiteResult, back_populates="run")
    cases = relationship("CaseResult", back_populates="run")
    project = relationship("Project", back_populates="runs")
