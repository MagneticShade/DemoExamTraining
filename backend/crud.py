from sqlalchemy.orm import Session
from models import User
from schemas import UserLogin,UserRegis 
import hashlib

def hash_pas(password:str):
    pas=password.encode("utf-8")
    hash_pas=hashlib.sha256(pas)
    res=hash_pas.hexdigest()
    return res

def get_users (db:Session):
    return db.query(User)

def user_check(db:Session,user:UserLogin):
    found=db.query(User).filter_by(login=user.login,password=hash_pas(user.password)).first()
    return found

def add_user(db:Session,user:UserRegis):
    user.password=hash_pas(user.password)
    db_user=User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user