############ ->>>>>>>>> sample 

# from sqlalchemy import String, Integer, Column, Boolean

# from database import Base, engine

# def create_tables():
#     Base.metadata.create_all(engine)

# class Person(Base):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True)
#     firstname = Column(String(40), nullable=False)
#     lastname = Column(String(40), nullable=False)
#     isMale = Column(Boolean)


# models.# models.py
from sqlalchemy import String, Integer, Column
from database import Base, engine

def create_tables():
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
