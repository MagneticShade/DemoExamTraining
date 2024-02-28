from database import Base
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

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

class Status(Base):
    __tablename__="status"
    id=Column(Integer,primary_key=True)
    status_name=Column(String(15),unique=True)

class Priority(Base):
    __tablename__="priority"
    id=Column(Integer,primary_key=True)
    priority_name=Column(String(15),unique=True)

class Replacement_parts(Base):
    __tablename__="replacement_parts"
    id=Column(Integer,primary_key=True)
    name=Column(String(40))
    price=Column(Integer)

class Malfunction(Base):
    __tablename__="malfunction"
    id=Column(Integer,primary_key=True)
    time_to_repair=Column(TIMESTAMP)
    break_reason=Column(String(255))
    actions_taken=Column(String(255))
    cost=Column(Integer)

class ReplacementPartsForMalfunction(Base):
    __tablename__="replacement_parts_for_malfunction"
    id=Column(Integer,primary_key=True)
    malfunction_type=Column(Integer,ForeignKey("malfunction.id"))
    replacement_part=Column(Integer,ForeignKey("replacement_parts.id"))

class Commision(Base):
    __tablename__="commision"
    id=Column(Integer,primary_key=True)
    unique_id=Column(String(25))
    prioriry=Column(Integer,ForeignKey("priority.id"))
    date=Column(TIMESTAMP,default=now)
    gadget_name=Column(String(25))
    malfunction_type=Column(Integer,ForeignKey("malfunction.id"))
    gadget_info=Column(String(100))
    client_id=Column(Integer,ForeignKey("user.id"))
    status=Column(Integer,ForeignKey("status.id"))
    date_of_completion=Column(TIMESTAMP)
    time_added=Column(TIMESTAMP)
    comment=Column(String(255))
    addendum=Column(String(255))
    priorities=relationship("Priority",back_populates="commisions")
    statuses=relationship("Status",back_populates="commisions")
    malfunctions=relationship("Malfunction",back_populates="commisions")

Priority.commisions=relationship("Commision",back_populates="priorities")
Status.commisions=relationship("Commision",back_populates="statuses")
Malfunction.commisions=relationship("Commision",back_populates="malfunctions")


class Task(Base):
    __tablename__="task"
    id=Column(Integer,primary_key=True)
    assignee_id=Column(Integer,ForeignKey("user.id"))
    commision_id=Column(Integer,ForeignKey("commision.id"))