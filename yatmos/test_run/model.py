from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class TestRun(Base):
    __tablename__ = "test_runs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    desc = Column(String)
    project_id = Column(Integer, ForeignKey("projects.id"))

    results = relationship("TestSuiteResult", back_populates="run")
    project = relationship("Project", back_populates="test_runs")
