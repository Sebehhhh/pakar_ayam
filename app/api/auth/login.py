from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta  # Tambahkan impor untuk timedelta
from app.core.security import create_access_token
from app.core.config import Config
from app.models.token import Token  # Pastikan modul ini diimpor jika digunakan

# ...

router = APIRouter()

@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implementasi logika login
    # ...

    # Menghasilkan token akses
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
