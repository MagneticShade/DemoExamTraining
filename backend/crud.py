from fastapi import HTTPException
from sqlalchemy.orm import Session
from hashlib import sha256
from models import User,Commision,Malfunction,Priority,Status
from schemas import UserLogin,UserRegis,Card

def hash(password:str)->str:
    enc=password.encode("utf-8")
    pas=sha256(enc)
    hexd=pas.hexdigest()
    return hexd

def get_user(user:UserLogin,db:Session):
    res=db.query(User).filter_by(login=user.login,password=hash(user.password)).first()
    return res

def add_user(user:UserRegis,db:Session):
    us_log=UserLogin(login=user.login,password=user.password)
    if get_user(us_log,db):
        raise HTTPException(400,detail="User already exists")
    
    user.password=hash(user.password)
    try:
        user_db=User(**user.model_dump(),role_id=3)
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
    except:
        raise HTTPException(status_code=400)

def get_card(id:int,db:Session):
    cards=db.query(Commision).filter_by(client_id=id).join(Malfunction).join(Priority).join(Status).all()
    return cards
