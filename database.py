from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL='postgresql://postgres:password@localhost/database_name'

engine=create_engine(DB_URL)

SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()