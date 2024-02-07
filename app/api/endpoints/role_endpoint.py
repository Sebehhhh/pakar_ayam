from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.models.role import Role
from app.api.crud.role_crud import create_role, get_role, delete_role, update_role
from app.db.session import get_db

router = APIRouter()

@router.post("/roles/", response_model=Role)
def create_role_endpoint(role_data: Role, db: Session = Depends(get_db)):
    db_role = create_role(db, role_data.dict())
    return db_role

@router.get("/roles/{role_id}", response_model=Role)
def get_role_by_id(role_id: int, db: Session = Depends(get_db)):
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/roles/{role_id}", response_model=Role)
def update_role_endpoint(role_id: int, role_data: Role, db: Session = Depends(get_db)):
    db_role = get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")

    updated_role = update_role(db, role_id, role_data.dict())
    return updated_role

@router.delete("/roles/{role_id}")
def delete_role_endpoint(role_id: int, db: Session = Depends(get_db)):
    if not delete_role(db, role_id):
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted successfully"}

# Tambahkan endpoint untuk mendapatkan semua peran (roles)
@router.get("/roles/", response_model=List[Role])
def get_all_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    return roles
