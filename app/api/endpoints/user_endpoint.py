from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from app.api.crud.user_crud import get_users_with_roles  # Menggunakan fungsi yang mengembalikan data bersama nama peran
from app.db.session import get_db

router = APIRouter()

@router.get("/users/", response_model=List[dict])  # Menggunakan dict sebagai model respons sementara
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users_with_roles(db=db, skip=skip, limit=limit)
    return users
