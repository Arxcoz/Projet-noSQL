from pydantic import BaseModel


class OperatorBase(BaseModel):
    weapon_id: int
    gq_id: int
    name: str
    nationality: str


class OperatorCreate(OperatorBase):
    pass


class Operator(OperatorBase):
    id: int
    weapon_id: int
    gq_id: int
    name: str
    nationality: str

    class Config:
        orm_mode = True


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
    vehicule_id: int


class MissionCreate(MissionBase):
    pass


class Mission(MissionBase):
    id: int
    target: str
    vehicule_id: int

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
