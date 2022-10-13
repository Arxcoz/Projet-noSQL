from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router = APIRouter()

#Fonction GET
@router.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)
                 ):
    return crud.create_weapon(db=db, weapon=weapon)

#Fonction POST
@router.get("/weapons/", response_model=list[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud.get_weapon(db, skip=skip, limit=limit)
    return weapons
