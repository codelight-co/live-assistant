from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

engine = create_engine('postgresql://postgres:postgres@localhost:5455/ai-chatbot')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
meta = MetaData()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

