from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_weapon

router = APIRouter()


# GET Function
@router.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    return crud_weapon.create_weapon(db=db, weapon=weapon)


# POST Function
@router.get("/weapons/", response_model=list[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud_weapon.get_weapon(db, skip=skip, limit=limit)
    return weapons
