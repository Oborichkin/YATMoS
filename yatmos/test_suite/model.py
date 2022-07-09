from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class TestSuite(Base):
    __tablename__ = "test_suites"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    desc = Column(String)
    parent_id = Column(Integer, ForeignKey("test_suites.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="test_suites")
    parent = relationship("TestSuite", remote_side=id, backref="children")
    results = relationship("TestSuiteResult", back_populates="suite")


class TestSuiteResult(Base):
    __tablename__ = "test_suite_results"
    id = Column(Integer, primary_key=True, index=True)
    result = Column(String)
    suite_id = Column(Integer, ForeignKey("test_suites.id"))
    run_id = Column(Integer, ForeignKey("test_runs.id"))

    run = relationship("TestRun", back_populates="results")
    suite = relationship("TestSuite", back_populates="results")
