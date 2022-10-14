from pydantic import BaseModel
from typing import Optional


# OPERATOR SCHEMAS

class OperatorBase(BaseModel):
    pass


class OperatorUpdate(BaseModel):
    weapon_id: int | None = None
    gq_id: int | None = None
    mission_id: int | None = None
    name: str | None = None
    nationality: str | None = None


class OperatorCreate(OperatorBase):
    weapon_id: int
    gq_id: int
    mission_id: int | None = None
    name: str
    nationality: str


class Operator(OperatorBase):
    id: int
    weapon_id: int
    gq_id: int
    mission_id: int | None
    name: str
    nationality: str

    class Config:
        orm_mode = True


# WEAPON SCHEMAS

class WeaponBase(BaseModel):
    name: str
    type: str


class WeaponCreate(WeaponBase):
    pass


class Weapon(WeaponBase):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True


class QGBase(BaseModel):
    country: str


class QGCreate(QGBase):
    pass


class QG(QGBase):
    id: int
    country: str

    class Config:
        orm_mode = True


class MissionBase(BaseModel):
    target: str
    vehicule_id: int | None


class MissionCreate(MissionBase):
    pass


class Mission(MissionBase):
    id: int
    target: str
    vehicule_id: int | None

    class Config:
        orm_mode = True


class VehiculeBase(BaseModel):
    name: str
    type: str


class VehiculeCreate(VehiculeBase):
    pass


class Vehicule(VehiculeBase):
    id: int
    name: str
    type: str

    class Config:
        orm_mode = True
