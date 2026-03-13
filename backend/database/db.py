from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Database_url = "sqlite:///./app.db"
UPLOAD_DIR = "uploads"


engine = create_engine(Database_url, connect_args={"check_same_thread":False})

sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind= engine)

Base = declarative_base()