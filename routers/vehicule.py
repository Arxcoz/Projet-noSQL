from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router = APIRouter()


@router.post("/vehicules/", response_model=schemas.Vehicule)
def create_vehicule(vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)
                   ):
    return crud.create_vehicule(db=db, vehicule=vehicule)


@router.get("/vehicules/", response_model=list[schemas.Vehicule])
def read_vehicule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicule = crud.get_vehicule(db, skip=skip, limit=limit)
    return vehicule
