# app/api/endpoints/role_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.role_crud import get_role
from app.models.role import Role
from app.db.session import get_db

router = APIRouter()

@router.get("/role/", response_model=List[Role])
def read_role(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        role = get_role(db=db, skip=skip, limit=limit)
        return role
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
