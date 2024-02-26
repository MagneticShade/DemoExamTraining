from fastapi import FastAPI,Depends,HTTPException,Header
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine,LocalSession
from models import Base
from schemas import UserLog,UserRegis,UserCard,Redirect,RoleEdit
from crud import get_user,add_user,get_card,get_roles,get_admin_card,edit_user_role

Base.metadata.create_all(bind=engine)

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/login/",response_model=Redirect)
def user_check(user:UserLog,db:Session=Depends(get_db)):
    found=get_user(db,user)
    if found:
        redir=Redirect(id=found.id,path="")
        match(found.role_id):

            case 3:
                redir.path="user.html"
            case 4:
                redir.path="admin.html"
            case 5:
                redir.path="manager.html"
            case 6:
                redir.path="master.html"

        return redir
                
            
    raise HTTPException(status_code=404)

@app.post("/user/create/",response_model=Redirect)
def user_create(user:UserRegis,db:Session=Depends(get_db)):
    id=add_user(user,db)
    return Redirect(id=id,path="user.html")

@app.get("/commisions/{id}",response_model=list[UserCard])
def get_commisions(id:int,db:Session=Depends(get_db)):

    commision=get_card(id,db)
    return commision

@app.get("/roles/")
def get_roles_names(db:Session=Depends(get_db)):
    roles=get_roles(db)
    return roles

@app.get("/admin/users/")
def get_users_admin(db:Session=Depends(get_db),admin_id: Annotated[str | None, Header()] = None):
    if admin_id is not None:
        cards=get_admin_card(db,admin_id)
        return cards
    raise HTTPException(status_code=403,detail="forbidden")

@app.patch("/admin/role/")
def change_role(role_edit:RoleEdit,db:Session=Depends(get_db),admin_id: Annotated[str | None, Header()] = None):
    if admin_id is not None:
        edit_user_role(db,role_edit.id,role_edit.role_id,admin_id)
    else:
        raise HTTPException(status_code=403,detail="forbidden")