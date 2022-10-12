from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas
import models
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/operators/", response_model=schemas.Operator)
def createOperator(operator: schemas.OperatorCreate, db: Session = Depends(get_db)):
    return crud.createOperator(db=db, operator=operator)


@app.get("/operators/", response_model=list[schemas.Operator])
def readOperators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operators = crud.getOperators(db, skip=skip, limit=limit)
    return operators


@app.get("/operators/{operator_id}", response_model=schemas.Operator)
def readOperator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud.getOperator(db, operator_id=operator_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_operator


@app.post("/weapons/", response_model=schemas.Weapon)
def createWeapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)
):
    return crud.createWeapon(db=db, weapon=weapon)


@app.get("/weapons/", response_model=list[schemas.Weapon])
def readWeapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud.getWeapon(db, skip=skip, limit=limit)
    return weapons

@app.post("/qg/", response_model=schemas.QG)
def createQG(qg: schemas.QGCreate, db: Session = Depends(get_db)
):
    return crud.createQG(db=db, qg=qg)

@app.get("/qg/", response_model=list[schemas.QG])
def readQG(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qg = crud.getQG(db, skip=skip, limit=limit)
    return qg