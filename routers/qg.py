from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router = APIRouter()


@router.post("/qg/", response_model=schemas.QG)
def create_qg(qg: schemas.QGCreate, db: Session = Depends(get_db)
             ):
    return crud.create_qg(db=db, qg=qg)


@router.get("/qg/", response_model=list[schemas.QG])
def read_qg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qg = crud.get_qg(db, skip=skip, limit=limit)
    return qg
