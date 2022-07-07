from datetime import date
from sqlalchemy.orm import Session
import models, schemas
from month import last_date_of_month

def get_ipo(db: Session, id: int):
    return db.query(models.IPO).filter(models.IPO.id == id).first()

def get_month_ipo(db: Session,year:int, month:str):
    _start_date, _end_date = last_date_of_month(year,month)
    return db.query(models.IPO).filter(models.IPO.close_date.between(_start_date, _end_date)).all()

def get_ipo_company(db: Session, company: str):
    return db.query(models.IPO).filter(models.IPO.company == company).first()

def get_active_ipo(db: Session, curr_date: date):
    return db.query(models.IPO).filter(models.IPO.close_date >= curr_date).all()

def get_ipo_date(db: Session, curr_date: date):
    return db.query(models.IPO).filter(models.IPO.close_date >= curr_date, models.IPO.open_date <= curr_date).all()
