from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router = APIRouter()

#Fonction GET
@router.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    return crud.create_weapon(db=db, weapon=weapon)

#Fonction POST
@router.get("/weapons/", response_model=list[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud.get_weapon(db, skip=skip, limit=limit)
    return weapons

#Fonction DELETE
@router.delete("/weapons/{weapon_id}")
def delete_weapon(weapon_id: int, db : Session = Depends(get_db)):
    db_operator = crud.get_operator_weapon(db=db,weapon_id=weapon_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator have this weapon assign")
    db_weapon = crud.delete_weapon(db, weapon_id=weapon_id)
    return "Weapon eliminated"

