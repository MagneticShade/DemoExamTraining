from sqlalchemy.orm import Session
from models import User,Commision,Priority,Status,Malfunction,Role
from schemas import UserLog,UserRegis,UserCard,AdminCard
from fastapi import HTTPException
from hashlib import sha256

def get_user(db:Session,user:UserLog):
    res=db.query(User).filter_by(login=user.login,password=hash(user.password)).first()
    return res

def hash(password:str)->str:
    enc=password.encode("utf-8")
    pas=sha256(enc)
    return pas.hexdigest()

def add_user(user:UserRegis,db:Session):
    if(user.login=="" or user.password=="" or user.name==""):
        raise HTTPException(400,detail="empty fields")
    user.password=hash(user.password)
    try:
        user_db=User(**user.model_dump(),role_id=3)
        db.add(user_db)
        db.commit()
        db.refresh(user_db)
    except:
        raise HTTPException(status_code=400,detail="bad_request")
    return user_db.id

def get_card(id:int,db:Session):
    cards=db.query(Commision,Priority,Malfunction,Status).filter_by(client_id=id).join(Priority).join(Malfunction).join(Status)
    print(cards)
    array=list[UserCard]()
    for commision,priority,malfunction,status in cards:
        
        array.append(UserCard(unique_id=commision.unique_id,
                          priority=priority.prioriry_name,
                          date=str(commision.date),
                          gadget_name=commision.gadget_name,
                          gadget_info=commision.gadget_info,
                          malfunction=malfunction.malfunction_name,
                          status=status.status_name,
                          date_of_completion=str(commision.date_of_completion),
                          time_added=str(commision.time_added)))

    return array

def get_roles(db:Session):
    return db.query(Role).all()

def get_admin_card(db:Session):
    users=db.query(User).all()
    array=list()
    for user in users:
        array.append(AdminCard(login=user.login,role_id=user.role_id))
    return array