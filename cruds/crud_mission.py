from fastapi import HTTPException
from sqlalchemy.orm import Session
from appsql import models, schemas


# GET function
def get_mission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Missions).offset(skip).limit(limit).all()


# Create function
def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Missions(target=mission.target, vehicule_id=mission.vehicule_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission
