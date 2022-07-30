from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    desc = Column(String)

    suites = relationship("Suite", back_populates="project")
    runs = relationship("Run", back_populates="project")
