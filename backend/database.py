from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_str="mysql+pymysql://root@localhost:3306/auth3"
engine=create_engine(connection_str,echo=True)
engine.connect()

SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()