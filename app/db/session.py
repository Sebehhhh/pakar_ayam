from sqlalchemy.orm import sessionmaker
from app.db.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
