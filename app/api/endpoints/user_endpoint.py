from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.role import Role
from app.api.crud.user_crud import get_users_with_roles, create_user, get_user
from app.db.session import get_db
from passlib.hash import bcrypt

router = APIRouter()

@router.get("/users/", response_model=List[dict])  # Menggunakan dict sebagai model respons sementara
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = get_users_with_roles(db=db, skip=skip, limit=limit)
    return users

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

@router.get("/users/{user_id}", response_model=dict)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    # Cari pengguna berdasarkan ID
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Kembalikan informasi pengguna
    return {
        'id': db_user.id,
        'nama': db_user.nama,
        'username': db_user.username,
        'role_id': db_user.role_id,
    }


@router.put("/users/{user_id}", response_model=dict)
def update_user_endpoint(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    # Pastikan pengguna yang akan diedit ada dalam basis data
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Perbarui data pengguna sesuai dengan input yang diberikan
    for key, value in user_data.items():
        if key == 'password':
            # Hash password baru menggunakan bcrypt jika ada
            value = bcrypt.hash(value)
        setattr(db_user, key, value)

    # Lakukan commit untuk menyimpan perubahan ke basis data
    db.commit()

    # Kembalikan data pengguna yang telah diperbarui bersama dengan nama peran
    return {
        'id': db_user.id,
        'nama': db_user.nama,
        'username': db_user.username,
        'password': db_user.password,  # Mengembalikan password tidak di-hash
        'role_id': db_user.role_id,
    }