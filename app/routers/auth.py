from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserOut
from app.repositories.users import UsersRepository
from app.database import get_db
from app.core.security import get_current_user, verify_password  

router = APIRouter()

@router.post("/signup", response_model=UserOut)
def signup(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = UsersRepository.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    new_user = UsersRepository.create_user(db, user_data)
    return new_user

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = UsersRepository.get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return {"message": "Successfully logged in!"}

@router.get("/profile", response_model=UserOut)
def profile(current_user: User = Depends(get_current_user)):
    return current_user
