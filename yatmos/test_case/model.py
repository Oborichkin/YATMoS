from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from ..database import Base
from ..test_step.model import TestStep  # FIXME: Remove this line


class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    desc = Column(String)
    suite_id = Column(Integer, ForeignKey("test_suites.id"))

    suite = relationship("TestSuite", backref="test_cases")
    steps = relationship("TestStep", order_by="TestStep.position", collection_class=ordering_list("position"))
