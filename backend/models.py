from database import Base
from sqlalchemy import Integer,String,Column,ForeignKey,Enum
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql.functions import now
from sqlalchemy.dialects.mysql import TIMESTAMP



class Role(Base):
    __tablename__ = 'role'
    id=mapped_column(Integer,primary_key=True)
    role_name=Column(String(30))

class User(Base):
    __tablename__ = 'user'
    id= mapped_column(Integer,primary_key=True)
    name= Column(String(30))
    login= Column(String(30))
    password= Column(String(70))
    role=mapped_column(Integer,ForeignKey('role.id'))


class Status(Base):
    __tablename__="status"
    id=mapped_column(Integer,primary_key=True)
    status_name=Column(String(30))

class malfunction(Base):
    __tablename__="malfunction"
    id=mapped_column(Integer,primary_key=True)
    malfunction_name=Column(String(30))


class Order(Base):
    
    __tablename__ = 'order'

    id=mapped_column(Integer,primary_key=True)
    date=Column(TIMESTAMP,default=now)
    device=Column(String(60))
    malfunction_type=mapped_column(Integer,ForeignKey('malfunction.id'))
    client_id=mapped_column(Integer,ForeignKey("user.id"))
    status_type=mapped_column(Integer,ForeignKey("status.id"))