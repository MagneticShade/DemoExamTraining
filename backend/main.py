from fastapi import FastAPI,HTTPException,Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from schemas import UserLogin,UserRegis
from models import Base
from database import engine,SessionLocal
from crud import user_get_all,user_add,user_check

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
    return user_get_all(db)

@app.post("/login/")
def user_login(user:UserLogin,db:Session=Depends(get_db)):
    found=user_check(db,user)
    if found:
        match(found):
            case 1:
                return RedirectResponse("user.html",status_code=302)
            case 2:
                return RedirectResponse("user.html",status_code=302)
            case 3:
                return RedirectResponse("user.html",status_code=302)
            case 4:
                return RedirectResponse("user.html",status_code=302)
            
    raise HTTPException(status_code=404)
