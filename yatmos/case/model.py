from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

from ..database import Base
from ..step.model import Step  # FIXME: Remove this line


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    desc = Column(String)
    suite_id = Column(Integer, ForeignKey("suites.id"))

    suite = relationship("Suite", backref="cases")
    steps = relationship("Step", order_by="Step.position", collection_class=ordering_list("position"))
