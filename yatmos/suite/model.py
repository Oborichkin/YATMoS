from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Suite(Base):
    __tablename__ = "suites"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    desc = Column(String)
    parent_id = Column(Integer, ForeignKey("suites.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="suites")
    parent = relationship("Suite", remote_side=id, backref="children")
    results = relationship("SuiteResult", back_populates="suite")


class SuiteResult(Base):
    __tablename__ = "suite_results"
    id = Column(Integer, primary_key=True, index=True)
    result = Column(String)
    suite_id = Column(Integer, ForeignKey("suites.id"))
    run_id = Column(Integer, ForeignKey("runs.id"))

    run = relationship("Run", back_populates="results")
    suite = relationship("Suite", back_populates="results")
