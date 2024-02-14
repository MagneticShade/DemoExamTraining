from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from models import Base
from schemas import UserLogin,UserRegis,Card,Redirect
from crud import get_user,add_user,get_card

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
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/login/",response_model=Redirect)
def user_check(user:UserLogin,db:Session=Depends(get_db)):
    found=get_user(user,db)
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

@app.get("/commisions/{id}")
def get_commisions(id:int,db:Session=Depends(get_db)):

    commision=get_card(id,db)
    return commision