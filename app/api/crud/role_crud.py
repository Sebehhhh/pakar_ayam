# app/api/crud/role_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.role import Role
from app.db.session import get_db

def get_role(db: Session, skip: int = 0, limit: int = 10) -> List[Role]:
    return db.query(Role).offset(skip).limit(limit).all()
