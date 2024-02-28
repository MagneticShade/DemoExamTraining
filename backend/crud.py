import schemas
from models import User,Commision,Role,Status,Malfunction,Priority
from sqlalchemy.orm import Session
from fastapi import HTTPException
from hashlib import sha256

def hash_password(password:str):
    enc=password.encode("utf-8")
    hashed=sha256(enc)
    digested=hashed.hexdigest()
    return digested

def authorize_user(db:Session,user_login:schemas.UserLogin):
    found=db.query(User).filter_by(login=user_login.login,password=hash_password(user_login.password)).first()
    if found:
        return found.id
    return None

def registrate_user(db:Session,user_regis:schemas.UserRegis):
    if(user_regis.login==""or user_regis.password=="" or user_regis.name==""):
        raise HTTPException(status_code=400,detail="empty fields")
    user_regis.password=hash_password(user_regis.password)
    try:
        user_db=User(**user_regis.model_dump(),role_id=3)
        db.add(user_db)
        db.commit()
        db.refresh()
    except Exception:
        raise HTTPException(status_code=400,detail="bad_request")
    
def get_card(db:Session,id:int):
    