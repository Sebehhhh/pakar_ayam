# app/models/role.py
from sqlmodel import SQLModel, Field

class Role(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    role: str
