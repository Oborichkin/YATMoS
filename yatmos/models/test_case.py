from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    desc = Column(String)
    suite_id = Column(Integer, ForeignKey("test_suites.id"))

    suite = relationship("TestSuite", backref="test_cases")
