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

