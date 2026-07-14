from fastapi import FastAPI
from database import engine,Base
from models import Game
from database import SessionLocal
from schemas import Creategame

from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext

from models import User
from schemas import UserCreate
from auth import create_access_token


from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from auth import verify_token
from fastapi.security import OAuth2PasswordRequestForm
from database import get_db
from sqlalchemy.orm import Session

app=FastAPI()
Base.metadata.create_all(bind=engine)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://game-store-react-js.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    print("Received token:", token)

    email = verify_token(token)

    print("Decoded email:", email)

    if email is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return email
    


@app.get("/")
def home():
    return{"game store API is running!!"}

@app.get("/games")
def getgames(current_user:str=Depends(get_current_user),
             db:Session=Depends(get_db)):
    
    games=db.query(Game).all()
   
    return games

@app.post("/register",status_code=201)
def register(user:UserCreate,
             db:Session=Depends(get_db)):
    
    existing_user=db.query(User).filter(
        User.email==user.email
    ).first()

    if existing_user:
     
     raise HTTPException(
        status_code=400,
        detail="Email already registered"
    )
    hashed_password=pwd_context.hash(user.password)

    new_user=User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
   
    db.refresh(new_user)
  

    return {"message": "User registered successfully"}


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db:Session=Depends(get_db)
):
    

    existing_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    if not pwd_context.verify(
        form_data.password,
        existing_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        {"sub": existing_user.email}
    )

    

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.post("/games")
def SetGame(
    game: Creategame,
    current_user: str = Depends(
        get_current_user),db:Session=Depends(get_db)
):

  


    new_game = Game(
        name=game.name,
        genre=game.genre,
        price=game.price,
        image=game.image
    )

    db.add(new_game)

    db.commit()

    db.refresh(new_game)

    

    return new_game


