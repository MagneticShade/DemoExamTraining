from pydantic import BaseModel

class UserLogin(BaseModel):
    login:str
    password:str

class UserRegis(BaseModel):
    name:str
    login:str
    password:str
    role:int