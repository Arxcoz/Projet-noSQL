from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_vehicule

router = APIRouter()


# GET Function
@router.get("/vehicules/", response_model=list[schemas.Vehicule])
def read_vehicule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicule = crud_vehicule.get_vehicule(db, skip=skip, limit=limit)
    return vehicule


# POST Function
@router.post("/vehicules/", response_model=schemas.Vehicule)
def create_vehicule(vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)):
    return crud_vehicule.create_vehicule(db=db, vehicule=vehicule)


