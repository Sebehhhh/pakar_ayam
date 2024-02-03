# app/models/post.py
from sqlmodel import SQLModel, Field

class Post(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    nama: str
    detail: str
    saran: str
    gambar: str
