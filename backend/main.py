from fastapi import FastAPI,Depends,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from models import Base

Base.metadata.create_all(bind=engine)

app=FastAPI()
