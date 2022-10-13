from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_mission

router = APIRouter()


# POST Function
@router.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud_mission.create_mission(db=db, mission=mission)


# GET Function
@router.get("/missions/", response_model=list[schemas.Mission])
def read_mission(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mission = crud_mission.get_mission(db, skip=skip, limit=limit)
    return mission
