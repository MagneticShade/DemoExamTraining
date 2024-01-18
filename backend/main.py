from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base
from database import engine,SessionLocal
from schemas import UserLogin,UserRegis
from crud import get_users,add_user,user_check

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

@app.get("/",response_model=list[UserLogin])
def user_all(db:Session=Depends(get_db)):
    users=get_users(db)
    if (users):
        return users
    
    raise HTTPException(status_code=404)


@app.post("/regis/")
def user_add(user:UserRegis,db:Session=Depends(get_db)):
    add_user(db,user)

@app.post("/login/")
def check_user(user:UserLogin,db:Session=Depends(get_db)):
    found=user_check(db,user)
    
    if (not found):
        raise HTTPException(status_code=404)
    
    match found.role:
        case 1:
            return RedirectResponse("http://localhost:5173/admin.html",status_code=302)
        case 2:
            return RedirectResponse("http://localhost:5173/user.html",status_code=302)
        case 3:
            return RedirectResponse("http://localhost:5173/manager.html",status_code=302)
        case 4:
            return RedirectResponse("http://localhost:5173/master.html",status_code=302)
    