from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Operators(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    weapon_id = Column(Integer, ForeignKey("weapons.id"))
    gq_id = Column(Integer, ForeignKey("general_quarter.id"))
    name = Column(String, index=True)
    nationality = Column(String, index=True)

    weapons = relationship("Weapons", back_populates="operators")
    general_quarter = relationship("general_quarter", back_populates="operators")


class Weapons(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String, index=True)

    operators = relationship("Operators", back_populates="weapons")

class GQ(Base):
    __tablename__ = "general_quarter"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)

    operators = relationship("Operators", back_populates="general_quarter")

class Mission(Base):
    __tablename__ = "mission"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)

    operators = relationship("Operators", back_populates="general_quarter")