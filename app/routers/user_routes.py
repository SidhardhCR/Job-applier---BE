from fastapi import APIRouter, HTTPException
from app.models import UserSignup,UserLogin
from app.crud import signup_user, login_user
from app.config import users_collection

router = APIRouter()

@router.post("/signup/")
async def signup(user: UserSignup):
    user_id = await signup_user(user, users_collection)
    return {"message": "User registered successfully", "user_id": user_id}

@router.post("/login/")
async def login(user: UserLogin):
    login_response = await login_user(user, users_collection)
    return login_response


