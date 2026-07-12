from database import Base 
from sqlalchemy import Column, Integer, String, Float

class Game (Base):
    __tablename__="games"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    genre=Column(String)
    price=Column(Float)
    image=Column(String)

    
          

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)

    username = Column(String, unique=True)

    email = Column(String, unique=True)

    password = Column(String)