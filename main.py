from fastapi import FastAPI, status
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()
db = SessionLocal()

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True

class User(OurBaseModel):
    id: int
    name: str 
    email: str


@app.get("/", response_model=list[User], status_code=status.HTTP_200_OK)
def getAll_Users():
    getAllUsers = db.query(models.User).all()
    return getAllUsers

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def add_User(user: User):
    newUser = models.User(
        id = user.id,
        name = user.name,
        email = user.email
    )

    db.add(newUser)
    db.commit()

    return newUser


@app.put("/update/{user_id}", response_model=User, status_code=status.HTTP_202_ACCEPTED)
def updatePerson(user_id: int, user: User):
    find_user = db.query(models.User).filter(models.User.id == user_id).first()
    find_user.id = user.id
    find_user.name = user.name
    find_user.email = user.email

    db.commit()
    return find_user