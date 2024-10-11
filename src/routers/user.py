from fastapi import APIRouter,HTTPException
from database.database import SessionLocal
from src.models.user import User
from src.schemas.user import UserCreate,UserReturn

user_router = APIRouter()

db= SessionLocal()


@user_router.get("/")
def hello():
    return "fhsdkfhsdjklfhjklsdhfjklasdhfjklsdahk"


@user_router.get("/get_all_user")
def get_all_user():
    all_user = db.query(User).all()
    if not all_user:
        raise HTTPException(status_code=404,detail="no entry found in user table ")
    return all_user

@user_router.post("/create_user",response_model=UserCreate)
def create_user(user_data : UserCreate):
    new_user = User(name = user_data.name,email = user_data.email,password = user_data.password)
    db.add(new_user)
    db.commit()
    return new_user

    
