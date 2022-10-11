from sqlalchemy.orm import Session

import schemas
import models


def getOperator(db: Session, operator_id: int):
    return db.query(models.Operators).filter(models.Operators.id == operator_id).first()


def getOperatorName(db: Session, name: str):
    return db.query(models.Operators).filter(models.Operators.name == name).first()


def getOperators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operators).offset(skip).limit(limit).all()


def createOperator(db: Session, operator: schemas.OperatorCreate, weapons_id: int):
    db_operator = models.Operators(name=operator.name, weapon_id=weapons_id)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


def getWeapon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weapons).offset(skip).limit(limit).all()


def createUserWeapon(db: Session, item: schemas.WeaponCreate):
    db_weapon = models.Weapons(**item.dict())
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon