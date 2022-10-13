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
def get_operator_name(db: Session, name: str):
    return db.query(models.Operators).filter(models.Operators.name == name).first()


# POST function
def create_operator(db: Session, operator: schemas.OperatorCreate):
    db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id, nationality=operator.nationality)
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
