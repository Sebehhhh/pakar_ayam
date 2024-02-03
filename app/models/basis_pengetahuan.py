# app/models/basis_pengetahuan.py
from sqlmodel import SQLModel, Field

class Basis_Pengetahuan(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    penyakit_id: int
    gejala_id: int
    mb: float
    md: float
