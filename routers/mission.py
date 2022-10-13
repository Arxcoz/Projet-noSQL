from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router = APIRouter()

#Fonction POST
@router.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    return crud.create_mission(db=db, mission=mission)

#Fonction GET
@router.get("/missions/", response_model=list[schemas.Mission])
def read_mission(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mission = crud.get_mission(db, skip=skip, limit=limit)
    return mission
