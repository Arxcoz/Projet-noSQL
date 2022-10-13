from fastapi import HTTPException
from sqlalchemy.orm import Session

from appsql import schemas, models

#Fonction GET
#Table operators

def get_operators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operators).offset(skip).limit(limit).all()

#Par ID
def get_operator(db: Session, operator_id: int):
    return db.query(models.Operators).filter(models.Operators.id == operator_id).first()

#Par nom
def get_operator_weapon(db: Session, weapon_id: int):
    return db.query(models.Operators).filter(models.Operators.weapon_id == weapon_id).first()

#Table weapons

def get_weapon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weapons).offset(skip).limit(limit).all()

#Table quarter_general

def get_qg(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GQ).offset(skip).limit(limit).all()

#Table vehicules

def get_vehicule(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicules).offset(skip).limit(limit).all()

#Table missions

def get_mission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Missions).offset(skip).limit(limit).all()

#Fonction POST
#Table operators

def create_operator(db: Session, operator: schemas.OperatorCreate):
    db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id, nationality=operator.nationality)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator

#Table weapons

def create_weapon(db: Session, weapon: schemas.WeaponCreate):
    db_weapon = models.Weapons(name=weapon.name, type=weapon.type)
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon

#Table quarter_general

def create_qg(db: Session, qg: schemas.QGCreate):
    db_qg = models.GQ(country=qg.country)
    db.add(db_qg)
    db.commit()
    db.refresh(db_qg)
    return db_qg

#Table vehicules

def create_vehicule(db: Session, vehicule: schemas.VehiculeCreate):
    db_vehicule = models.Vehicules(name=vehicule.name, type=vehicule.type)
    db.add(db_vehicule)
    db.commit()
    db.refresh(db_vehicule)
    return db_vehicule

#Table missions

def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Missions(target=mission.target, vehicule_id=mission.vehicule_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission


#Fonction DELETE
#Table operators

def delete_operator(db: Session, operator_id: int):
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db.delete(db_operator)
    db.commit()
    return db_operator

def delete_weapon(db: Session, weapon_id: int):
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db.delete(db_weapon)
    db.commit()
    return db_weapon