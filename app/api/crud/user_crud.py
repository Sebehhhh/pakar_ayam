from sqlalchemy.orm import Session
from app.models.user import User
from app.models.role import Role

def get_users_with_roles(db: Session, skip: int = 0, limit: int = 10):
    query = (
        db.query(User.id, User.nama, User.username, User.password, User.role_id, Role.role)
        .join(Role, User.role_id == Role.id)
        .offset(skip)
        .limit(limit)
        .all()
    )
    
    users_with_roles = [
        {
            'id': user.id,
            'nama': user.nama,
            'username': user.username,
            'password': user.password,
            'role_id': user.role_id,
            'role': user.role
        } for user in query
    ]
    
    return users_with_roles

def create_user(db: Session, user_data: dict):
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def delete_user(db: Session, user_id: int):
    # Cari pengguna berdasarkan ID
    user_to_delete = db.query(User).filter(User.id == user_id).first()
    if user_to_delete:
        # Hapus pengguna dari basis data
        db.delete(user_to_delete)
        db.commit()
        return True
    return False
