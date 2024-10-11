from database.database import Base
from sqlalchemy import Column, String
import uuid

class ToDo(Base):
    __tablename__ = "todos"
    id = Column(String(50),primary_key=True,default=str(uuid.uuid4()))
    name = Column(String(20),nullable=False)
    description = Column(String(30),nullable=False)