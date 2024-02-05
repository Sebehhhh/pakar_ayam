# app/models/user.py
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    username: str
    password: str
    nama: str
    role_id: int
