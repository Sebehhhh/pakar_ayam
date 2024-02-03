from typing import Any, Dict
from jose import JWTError, jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.core.config import Config

# ... 

SECRET_KEY = Config.SECRET_KEY
ALGORITHM = "HS256"

# ...
