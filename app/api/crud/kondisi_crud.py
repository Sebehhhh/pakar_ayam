# app/api/crud/kondisi_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.kondisi import Kondisi
from app.db.session import get_db

def get_kondisi(db: Session, skip: int = 0, limit: int = 10) -> List[Kondisi]:
    return db.query(Kondisi).offset(skip).limit(limit).all()
