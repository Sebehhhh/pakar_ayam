# app/api/crud/user_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.user import User

def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()
