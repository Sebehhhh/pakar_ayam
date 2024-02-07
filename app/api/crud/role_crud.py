from sqlalchemy.orm import Session
from app.models.role import Role

def create_role(db: Session, role_data: dict):
    db_role = Role(**role_data)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_role(db: Session, role_id: int):
    return db.query(Role).filter(Role.id == role_id).first()

def update_role(db: Session, role_id: int, role_data: dict):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role:
        for key, value in role_data.items():
            setattr(db_role, key, value)
        db.commit()
        db.refresh(db_role)
        return db_role
    return None


def delete_role(db: Session, role_id: int):
    # Cari peran berdasarkan ID
    role_to_delete = db.query(Role).filter(Role.id == role_id).first()
    if role_to_delete:
        # Hapus peran dari basis data
        db.delete(role_to_delete)
        db.commit()
        return True
    return False
