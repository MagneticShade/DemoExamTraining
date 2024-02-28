from pydantic import BaseModel

class UserLogin(BaseModel):
    login:str
    password:str

class UserRegis(BaseModel):
    name:str
    login:str
    password:str

class Redirect(BaseModel):
    id:int
    path:str

class Roles(BaseModel):
    id:int
    role_name:str

class UserCard(BaseModel):
    unique_id:str
    priority:str
    date:str
    gadget_name:str
    malfunction_type:str
    gadget_info:str
    status:str
    date_of_completion:str|None
    time_aded:str|None
    comment:str|None
    addendum:str|None

class AdminCard(BaseModel):
    id:int
    login:str
    role_id:int