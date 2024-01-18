from database import Base
from sqlalchemy import Column,String,Integer,ForeignKey,TIMESTAMP
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.functions import now


class Role(Base):
    __tablename__="role"

    id=mapped_column(Integer,primary_key=True)
    role_name=Column(String(15))

class User(Base):
    __tablename__="user"

    id=mapped_column(Integer,primary_key=True)
    name=Column(String(25))
    login=Column(String(25))
    password=Column(String(70))
    role=mapped_column(Integer,ForeignKey("role.id"))

class Order(Base):
    __tablename__="order"

    id=Column(Integer,primary_key=True)
    date=Column(TIMESTAMP,default=now)
    device=Column(String(20))
    malfunction_type
    client=mapped_column(Integer,ForeignKey("user.id"))
    status
