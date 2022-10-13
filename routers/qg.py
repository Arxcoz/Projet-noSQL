from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
from cruds import crud_qg

router = APIRouter()


# POST Function
@router.post("/qg/", response_model=schemas.QG)
def create_qg(qg: schemas.QGCreate, db: Session = Depends(get_db)):
    return crud_qg.create_qg(db=db, qg=qg)


# GET Function
@router.get("/qg/", response_model=list[schemas.QG])
def read_qg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qg = crud_qg.get_qg(db, skip=skip, limit=limit)
    return qg
