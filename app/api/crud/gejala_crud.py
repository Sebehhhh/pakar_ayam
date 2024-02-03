# app/api/crud/gejala_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.gejala import Gejala
from app.db.session import get_db

def get_gejala(db: Session, skip: int = 0, limit: int = 10) -> List[Gejala]:
    return db.query(Gejala).offset(skip).limit(limit).all()
