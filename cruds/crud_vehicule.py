from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_vehicule(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicules).offset(skip).limit(limit).all()


# Create function
def create_vehicule(db: Session, vehicule: schemas.VehiculeCreate):
    db_vehicule = models.Vehicules(name=vehicule.name, type=vehicule.type)
    db.add(db_vehicule)
    db.commit()
    db.refresh(db_vehicule)
    return db_vehicule
