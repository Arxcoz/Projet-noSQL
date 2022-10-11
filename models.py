from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Operators(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    weapon_id = Column(Integer, ForeignKey("weapons.id"))

    weapons = relationship("weapons", back_populates="operators")


class Weapons(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)

    operators = relationship("operators", back_populates="weapons")