# app/api/endpoints/basis_pengetahuan_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.basis_pengetahuan_crud import get_basis_pengetahuan
from app.models.basis_pengetahuan import Basis_Pengetahuan
from app.db.session import get_db

router = APIRouter()

@router.get("/basis_pengetahuan/", response_model=List[Basis_Pengetahuan])
def read_basis_pengetahuan(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        basis_pengetahuan = get_basis_pengetahuan(db=db, skip=skip, limit=limit)
        return basis_pengetahuan
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
