# app/models/hasil.py
from sqlmodel import SQLModel, Field

class Hasil(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    tanggal: str
    penyakit: str
    gejala: str
    nilai: float
