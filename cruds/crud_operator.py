from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas
from fastapi.encoders import jsonable_encoder


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


def patch_operator(operator_id: int, db: Session, operator: schemas.OperatorUpdate):
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    if operator.weapon_id is not None:
        db_operator.weapon_id = operator.weapon_id
    if operator.gq_id is not None:
        db_operator.gq_id = operator.gq_id
    if operator.name is not None:
        db_operator.name = operator.name
    if operator.nationality is not None:
        db_operator.nationality = operator.nationality
    if operator.mission_id is not None:
        db_operator.mission_id = operator.mission_id
    db.commit()
    return db_operator
