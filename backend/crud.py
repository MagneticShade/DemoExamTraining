from sqlalchemy.orm import Session
from hashlib import sha256
from models import User,Commision,Malfunction,Priority,Status
from schemas import UserLogin

def hash(password:str)->str:
    enc=password.encode("utf-8")
    pas=sha256(enc)
    hexd=pas.hexdigest()
    return hexd

def get_user(user:UserLogin):