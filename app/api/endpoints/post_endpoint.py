# app/api/endpoints/post_endpoint.py
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from pytest import Session
from app.api.crud.post_crud import get_post
from app.models.post import Post
from app.db.session import get_db

router = APIRouter()

@router.get("/post/", response_model=List[Post])
def read_post(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        post = get_post(db=db, skip=skip, limit=limit)
        return post
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
