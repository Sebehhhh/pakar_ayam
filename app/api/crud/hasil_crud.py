# app/api/crud/hasil_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.hasil import Hasil
from app.db.session import get_db

def get_hasil(db: Session, skip: int = 0, limit: int = 10) -> List[Hasil]:
    return db.query(Hasil).offset(skip).limit(limit).all()
