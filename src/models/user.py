from database.database import Base
from sqlalchemy import Column, String
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String(50),primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(20),nullable=False)
    email = Column(String(30),nullable=False)
    password = Column(String(100),nullable=False)