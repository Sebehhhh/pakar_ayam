# app/api/endpoints/user_endpoint.py
from fastapi import APIRouter, Depends
from typing import List

from pytest import Session
from app.api.crud.user_crud import get_users
from app.models.user import User
from app.db.session import get_db

router = APIRouter()

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users(db=db, skip=skip, limit=limit)
    return users
