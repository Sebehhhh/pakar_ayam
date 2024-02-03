# app/api/crud/penyakit_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.penyakit import Penyakit
from app.db.session import get_db

def get_penyakit(db: Session, skip: int = 0, limit: int = 10) -> List[Penyakit]:
    return db.query(Penyakit).offset(skip).limit(limit).all()
