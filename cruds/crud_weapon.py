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
