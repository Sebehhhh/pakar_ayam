# app/api/endpoints/kondisi_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.kondisi_crud import get_kondisi
from app.models.kondisi import Kondisi
from app.db.session import get_db

router = APIRouter()

@router.get("/kondisi/", response_model=List[Kondisi])
def read_kondisi(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        kondisi = get_kondisi(db=db, skip=skip, limit=limit)
        return kondisi
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
