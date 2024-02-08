from pydantic import BaseModel

class UserLogin(BaseModel):
    login:str
    password:str

class UserRegis(BaseModel):
    name:str
    login:str
    password:str

class Card(BaseModel):
    unique_id:str
    priority:str
    date:str
    gadget_name:str
    gadget_info:str
    malfunction:str
    status:str
    date_of_completion:str|None
    time_added:str|None

class Redirect(BaseModel):
    id:int
    path:str