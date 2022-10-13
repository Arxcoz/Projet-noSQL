from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas, models, crud
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
def create_operator(operator: schemas.OperatorCreate, db: Session = Depends(get_db)):
    return crud.createOperator(db=db, operator=operator)


@app.get("/operators/", response_model=list[schemas.Operator])
def read_operators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    operators = crud.getOperators(db, skip=skip, limit=limit)
    return operators


@app.get("/operators/{operator_id}", response_model=schemas.Operator)
def read_operator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = crud.getOperator(db, operator_id=operator_id)
    if db_operator is None:
        raise HTTPException(status_code=404, detail="Operator not found")
    return db_operator

@app.delete("/operators/{operator_id}")
def remove_operator(self, db: Session, *, operator_id: int):
    db_operator = db.query(self.model).get(operator_id)
    db.delete(db_operator)
    db.commit()
    return db_operator

@app.post("/weapons/", response_model=schemas.Weapon)
def create_weapon(weapon: schemas.WeaponCreate, db: Session = Depends(get_db)):
    return crud.createWeapon(db=db, weapon=weapon)


@app.get("/weapons/", response_model=list[schemas.Weapon])
def read_weapon(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    weapons = crud.getWeapon(db, skip=skip, limit=limit)
    return weapons

@app.post("/qg/", response_model=schemas.QG)
def create_qg(qg: schemas.QGCreate, db: Session = Depends(get_db)
):
    return crud.createQG(db=db, qg=qg)

@app.get("/qg/", response_model=list[schemas.QG])
def read_qg(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    qg = crud.getQG(db, skip=skip, limit=limit)
    return qg

@app.post("/vehicules/", response_model=schemas.Vehicule)
def create_vehicule(vehicule: schemas.VehiculeCreate, db: Session = Depends(get_db)
):
    return crud.createVehicule(db=db, vehicule=vehicule)

@app.get("/vehicules/", response_model=list[schemas.Vehicule])
def read_vehicule(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vehicule = crud.getVehicule(db, skip=skip, limit=limit)
    return vehicule

@app.post("/missions/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)
):
    return crud.createMission(db=db, mission=mission)

@app.get("/missions/", response_model=list[schemas.Mission])
def read_mission(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mission = crud.getMission(db, skip=skip, limit=limit)
    return mission