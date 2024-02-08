from sqlalchemy import Column,Integer,String,ForeignKey,TIMESTAMP
from sqlalchemy.sql.functions import now

from database import Base

class Role(Base):
    __tablename__="role"
    id=Column(Integer,primary_key=True)
    role_name=Column(String(12),unique=True)

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(15))
    login=Column(String(15),unique=True)
    password=Column(String(70))
    role_id=Column(Integer,ForeignKey("role.id"))

class Malfunction(Base):
    __tablename__="malfunction"
    id=Column(Integer,primary_key=True)
    malfunction_name=Column(String(50),unique=True)
    time_to_repair=Column(TIMESTAMP)
    break_reason=Column(String(255))
    actions_taken=Column(String(255))
    cost=Column(Integer)

class ReplacementParts(Base):
    __tablename__="replacement_parts"
    id=Column(Integer,primary_key=True)
    name=Column(String(40))
    price=Column(Integer)

class ReplacementPartsForMalfunction(Base):
    __tablename__="replacement_parts_for_malfunction"
    id=Column(Integer,primary_key=True)
    malfunction_type=Column(Integer,ForeignKey("malfunction.id"))
    replacement_part=Column(Integer,ForeignKey("replacement_parts.id"))

class Priority(Base):
    __tablename__="priority"
    id=Column(Integer,primary_key=True)
    prioriry_name=Column(String(15),unique=True)

class Status(Base):
    __tablename__="status"
    id=Column(Integer,primary_key=True)
    status_name=Column(String(15))

class Commision(Base):
    __tablename__="commision"
    id=Column(Integer,primary_key=True)
    prioriry=Column(Integer,ForeignKey("priority.id"))
    date=Column(TIMESTAMP,default=now)
    gadget_name=Column(String(255))
    malfunction_type=Column(Integer,ForeignKey("malfunction.id"))
    gadget_info=Column(String(255))
    client_id=Column(Integer,ForeignKey("user.id"))
    status=Column(Integer,ForeignKey("status.id"))
    date_of_completion=Column(TIMESTAMP)
    time_added=Column(TIMESTAMP)
    comments=Column(String(255))
    addendum=Column(String(255))

class Task(Base):
    __tablename__="task"
    id=Column(Integer,primary_key=True)
    assignee_id=Column(Integer,ForeignKey("user.id"))
    commision_id=Column(Integer,ForeignKey("commision.id"))
