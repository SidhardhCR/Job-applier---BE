from fastapi import APIRouter, HTTPException
from app.models import UserSignup, UserLogin, ResumeData
from app.crud import signup_user, login_user, user_job_description
from app.config import users_collection, user_job_details


router = APIRouter()


@router.post("/signup/")
async def signup(user: UserSignup):
    user_id = await signup_user(user, users_collection)
    return {"message": "User registered successfully", "user_id": user_id}


@router.post("/login/")
async def login(user: UserLogin):
    login_response = await login_user(user, users_collection)
    return login_response


@router.post("/resume-submit")
async def resume_submit(data: ResumeData):
    submit_response = await user_job_description(data, user_job_details)
    # Call another route inside this route
    router.get("/scrape-jobs/{data.user_id}")
    return {"message": "Resume submitted successfully"}
