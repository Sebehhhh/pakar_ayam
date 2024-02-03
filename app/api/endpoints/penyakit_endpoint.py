# app/api/endpoints/penyakit_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.penyakit_crud import get_penyakit
from app.models.penyakit import Penyakit
from app.db.session import get_db

router = APIRouter()

@router.get("/penyakit/", response_model=List[Penyakit])
def read_penyakit(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        penyakit = get_penyakit(db=db, skip=skip, limit=limit)
        return penyakit
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
