from fastapi import HTTPException
from sqlalchemy.orm import Session

from appsql import models, schemas


# GET Function
def get_operators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operators).offset(skip).limit(limit).all()


# Par ID
def get_operator(db: Session, operator_id: int):
    return db.query(models.Operators).filter(models.Operators.id == operator_id).first()


# Par nom
def get_operator_weapon(db: Session, weapon_id: int):
    return db.query(models.Operators).filter(models.Operators.weapon_id == weapon_id).first()


# POST function
def create_operator(db: Session, operator: schemas.OperatorCreate):
    db_weapon = db.query(models.Operators).filter(models.Weapons.id == operator.weapon_id).first()
    if db_weapon is None and operator.weapon_id is not None:
        raise HTTPException(status_code=404, detail="This weapon don't exist")
    db_qg = db.query(models.GQ).filter(models.GQ.id == operator.gq_id).first()
    if db_qg is None and operator.gq_id is not None:
        raise HTTPException(status_code=404, detail="This general quarter don't exist")
    if operator.weapon_id is not None and operator.gq_id is not None:
        db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id, nationality=operator.nationality)
    elif operator.weapon_id is None and operator.gq_id is not None:
        db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, nationality=operator.nationality)
    else:
        db_operator = models.Operators(name=operator.name, nationality=operator.nationality)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


# DELETE function
def delete_operator(db: Session, operator_id: int):
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db.delete(db_operator)
    db.commit()
    return db_operator

# PATCH function
def patch_operator_weapon(db: Session, operator_id:int, weapon_id: int | None):
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == weapon_id).first()
    if db_weapon is None and weapon_id is not None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.weapon_id = weapon_id
    db.commit()
    return db_operator


def patch_operator_mission(db: Session, operator_id:int, mission_id: int | None):
    db_mission = db.query(models.Missions).filter(models.Missions.id == mission_id).first()
    if db_mission is None and mission_id is not None:
        raise HTTPException(status_code=404, detail="Mission not found")
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.weapon_id = mission_id
    db.commit()
    return db_operator

def patch_operator_qg(db: Session, operator_id:int, qg_id: int | None):
    db_qg = db.query(models.GQ).filter(models.GQ.id == qg_id).first()
    if db_qg is None and qg_id is not None:
        raise HTTPException(status_code=404, detail="Quarter general not found")
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.qg_id = qg_id
    db.commit()
    return db_operator
