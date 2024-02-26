from pydantic import BaseModel

class UserLog(BaseModel):
    login:str
    password:str

class UserRegis(BaseModel):
    name:str
    login:str
    password:str

class Role(BaseModel):
    id:int
    role_name:str

class Redirect(BaseModel):
    id:int
    path:str

class UserCard(BaseModel):
    unique_id:str
    priority:str
    date:str
    gadget_name:str
    gadget_info:str
    malfunction:str
    status:str
    date_of_completion:str|None
    time_added:str|None

class AdminCard(BaseModel):
    id:int
    login:str
    role_id:int

class RoleEdit(BaseModel):
    id:int
    role_id:int