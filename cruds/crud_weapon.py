from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_weapon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weapons).offset(skip).limit(limit).all()


# Create function
def create_weapon(db: Session, weapon: schemas.WeaponCreate):
    db_weapon = models.Weapons(name=weapon.name, type=weapon.type)
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon


# DELETE function
def delete_weapon(db: Session, weapon_id: int):
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == weapon_id).first()
    if db_weapon is None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db.delete(db_weapon)
    db.commit()
    return db_weapon


# PATCH function
def patch_operator_weapon(db: Session, operator_id: int, weapon_id: int | None):
    db_weapon = db.query(models.Weapons).filter(models.Weapons.id == weapon_id).first()
    if db_weapon is None and weapon_id is not None:
        raise HTTPException(status_code=404, detail="Weapon not found")
    db_operator = db.query(models.Operators).filter(models.Operators.id == operator_id).first()
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    db_operator.weapon_id = weapon_id
    db.commit()
    return db_operator
