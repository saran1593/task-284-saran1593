from database.db import Base
from sqlalchemy import Integer, Column, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True )
    name = Column( String, nullable = False)
    email = Column(String , unique= True, nullable= False)
    password = Column (String, nullable=False)