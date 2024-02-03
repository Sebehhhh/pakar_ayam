# app/api/endpoints/gejala_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.gejala_crud import get_gejala
from app.models.gejala import Gejala
from app.db.session import get_db

router = APIRouter()

@router.get("/gejala/", response_model=List[Gejala])
def read_gejala(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        gejala = get_gejala(db=db, skip=skip, limit=limit)
        return gejala
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
