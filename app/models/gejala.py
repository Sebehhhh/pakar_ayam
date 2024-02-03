# app/models/gejala.py
from sqlmodel import SQLModel, Field

class Gejala(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    nama: str
