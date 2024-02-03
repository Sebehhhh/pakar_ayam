from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    # Database Configuration
    DATABASE_URL = str(env_path.get("DATABASE_URL"))

    # JWT Secret Key
    SECRET_KEY = str(env_path.get("SECRET_KEY"))

    # Debug Mode
    DEBUG = env_path.get("DEBUG").lower() == "true"

    # CORS Configuration
    ALLOWED_HOSTS = env_path.get("ALLOWED_HOSTS", "").split(",")

    # Additional Configurations...
