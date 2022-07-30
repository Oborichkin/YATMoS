from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Step(Base):
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(Integer)
    title = Column(String, unique=True)
    desc = Column(String)
    case_id = Column(Integer, ForeignKey("cases.id"))
