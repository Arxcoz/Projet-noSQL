from sqlalchemy.orm import Session

from appsql import schemas, models


def get_operator(db: Session, operator_id: int):
    return db.query(models.Operators).filter(models.Operators.id == operator_id).first()


def get_operatorName(db: Session, name: str):
    return db.query(models.Operators).filter(models.Operators.name == name).first()


def get_operators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Operators).offset(skip).limit(limit).all()


def create_operator(db: Session, operator: schemas.OperatorCreate):
    db_operator = models.Operators(name=operator.name, gq_id=operator.gq_id, weapon_id=operator.weapon_id, nationality=operator.nationality)
    db.add(db_operator)
    db.commit()
    db.refresh(db_operator)
    return db_operator


def get_weapon(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Weapons).offset(skip).limit(limit).all()


def create_weapon(db: Session, weapon: schemas.WeaponCreate):
    db_weapon = models.Weapons(name=weapon.name, type=weapon.type)
    db.add(db_weapon)
    db.commit()
    db.refresh(db_weapon)
    return db_weapon


def get_qg(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GQ).offset(skip).limit(limit).all()


def create_qg(db: Session, qg: schemas.QGCreate):
    db_qg = models.GQ(country=qg.country)
    db.add(db_qg)
    db.commit()
    db.refresh(db_qg)
    return db_qg


def get_vehicule(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vehicules).offset(skip).limit(limit).all()


def create_vehicule(db: Session, vehicule: schemas.VehiculeCreate):
    db_vehicule = models.Vehicules(name=vehicule.name, type=vehicule.type)
    db.add(db_vehicule)
    db.commit()
    db.refresh(db_vehicule)
    return db_vehicule


def get_mission(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Missions).offset(skip).limit(limit).all()


def create_mission(db: Session, mission: schemas.MissionCreate):
    db_mission = models.Missions(target=mission.target, vehicule_id=mission.vehicule_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)
    return db_mission
