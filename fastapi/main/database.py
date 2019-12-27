import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbname, dbuser, dbpass, dbhost = (
    os.getenv('FASTAPI_DB_NAME'),
    os.getenv('FASTAPI_DB_USER'),
    os.getenv('FASTAPI_DB_PASSWORD'),
    os.getenv('FASTAPI_DB_HOST'),
)
SQLALCHEMY_DATABASE_URL = f'postgresql://{dbuser}:{dbpass}@postgresserver/{dbname}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
