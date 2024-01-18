from sqlalchemy.orm import Session
from models import User,Order
from schemas import UserRegis,UserLogin
import hashlib 

def hash_password(password:str):
   pas=password.encode("utf-8")
   pas_hash=hashlib.sha256(pas).hexdigest()
   return pas_hash



def user_get_all(db:Session):
   return db.query(User)



def user_add(db:Session, user:UserRegis):
    user.password=hash_password(user.password)
    db_user=User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

def user_check(db:Session,user:UserLogin):
    found=db.query(User).filter_by(login=user.login,password=hash_password(user.password)).first()
    if found:
        return found.role
    return None

