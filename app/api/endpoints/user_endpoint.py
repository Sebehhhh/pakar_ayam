from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.role import Role
from app.api.crud.user_crud import get_users_with_roles, create_user 
from app.db.session import get_db

router = APIRouter()

@router.get("/users/", response_model=List[dict])  # Menggunakan dict sebagai model respons sementara
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users_with_roles(db=db, skip=skip, limit=limit)
    return users

from passlib.hash import bcrypt

@router.post("/users/", response_model=dict)
def create_user_endpoint(user_data: dict, db: Session = Depends(get_db)):
    # Pastikan data peran yang diberikan ada dalam basis data
    role_id = user_data.get('role_id')
    role = db.query(Role).filter(Role.id == role_id).first()
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    # Hash password menggunakan bcrypt
    hashed_password = bcrypt.hash(user_data['password'])

    # Ganti password yang diberikan dengan hashed password
    user_data['password'] = hashed_password

    # Buat pengguna baru menggunakan fungsi CRUD
    db_user = create_user(db, user_data)

    # Kembalikan data pengguna yang telah ditambahkan bersama dengan nama peran
    return {
        'id': db_user.id,
        'nama': db_user.nama,
        'username': db_user.username,
        'password': hashed_password,  # Mengembalikan hashed password
        'role_id': db_user.role_id,
        'role': role.role  # Mengambil nama peran dari objek Role
    }
