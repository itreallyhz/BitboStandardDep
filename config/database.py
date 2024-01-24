from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import databases
import sqlalchemy

from dotenv import load_dotenv
import os

load_dotenv()

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:database@localhost:5432/Abitbo"
# DATABASE_URL = "postgresql://mhzqmzrmatxeof:e1bc11fbf873e05b304c222d7de46d5937ed49ae0a6b4d63e03137eb4effc4fc@ec2-54-234-13-16.compute-1.amazonaws.com:5432/d851asqogq01o7"
DATABASE_URL = os.getenv('DATABASE_URL_KEY')

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()