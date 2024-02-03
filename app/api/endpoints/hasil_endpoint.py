# app/api/endpoints/hasil_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.hasil_crud import get_hasil
from app.models.hasil import Hasil
from app.db.session import get_db

router = APIRouter()

@router.get("/hasil/", response_model=List[Hasil])
def read_hasil(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        hasil = get_hasil(db=db, skip=skip, limit=limit)
        return hasil
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
