# app/db/session.py
from sqlalchemy.orm import Session
from app.db.base import SessionLocal

def get_db() -> Session:
    db = SessionLocal()
    return db
