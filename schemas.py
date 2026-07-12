from pydantic import BaseModel



class Creategame(BaseModel):
   name:str
   genre:str
   price:float
   image:str


class UserCreate(BaseModel):
   username:str
   email:str
   password:str

class UserLogin(BaseModel):
   email:str
   password:str