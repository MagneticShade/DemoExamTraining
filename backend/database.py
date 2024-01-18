from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection_string="mysql+pymysql://root:@localhost:3306/auth4"

engine=create_engine(connection_string,echo=True)
engine.connect()
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()