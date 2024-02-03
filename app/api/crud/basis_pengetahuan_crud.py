# app/api/crud/basis_pengetahuan_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.basis_pengetahuan import Basis_Pengetahuan
from app.db.session import get_db

def get_basis_pengetahuan(db: Session, skip: int = 0, limit: int = 10) -> List[Basis_Pengetahuan]:
    return db.query(Basis_Pengetahuan).offset(skip).limit(limit).all()
