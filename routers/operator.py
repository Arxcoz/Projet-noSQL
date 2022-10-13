from fastapi import Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from depedency import get_db
from appsql import schemas
import crud


router=APIRouter()

#Fonction POST

@router.post("/operators/", response_model=schemas.Operator)
def create_operator(operator: schemas.OperatorCreate, db: Session = Depends(get_db)):
    return crud.create_operator(db=db, operator=operator)

#Fonction GET

@router.get("/operators/", response_model=list[schemas.Operator])
def read_operators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operators = crud.get_operators(db, skip=skip, limit=limit)
    return operators

#Par ID
@router.get("/operators/{operator_id}", response_model=schemas.Operator)
def read_operator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud.get_operator(db, operator_id=operator_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    return db_operator

#Fonction DELETE

@router.delete("/operators/{operator_id}")
def delete_operator(operator_id: int, db : Session = Depends(get_db)):
    db_operator = crud.delete_operator(db, operator_id=operator_id)
    return "Operator eliminated"
