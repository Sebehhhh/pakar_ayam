# app/api/crud/post_crud.py
from sqlalchemy.orm import Session
from typing import List
from app.models.post import Post
from app.db.session import get_db

def get_post(db: Session, skip: int = 0, limit: int = 10) -> List[Post]:
    return db.query(Post).offset(skip).limit(limit).all()
