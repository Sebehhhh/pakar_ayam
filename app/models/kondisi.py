# app/models/kondisi.py
from sqlmodel import SQLModel, Field

class Kondisi(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    kondisi: str
