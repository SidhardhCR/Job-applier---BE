from fastapi import APIRouter, HTTPException
from app.models import UserSignup, UserLogin, ResumeData
from app.crud import signup_user, login_user, user_job_description
from app.config import users_collection, user_job_details,matching_Jobs
from bson import ObjectId

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
    return {"submit_response": submit_response}

@router.get("/getUserJobDisc/")
async def getUserJobDescription():
    """Fetches all user job descriptions from the database."""
    try:
        descriptions = await user_job_details.find().to_list(None)  # Get all job descriptions
        
        if not descriptions:
            return {"message": "No job descriptions found."}

        # Convert ObjectId fields to strings for JSON serialization
        for desc in descriptions:
            if "_id" in desc:
                desc["_id"] = str(desc["_id"])  # Convert _id to string
            
            if "user_id" in desc and isinstance(desc["user_id"], ObjectId):
                desc["user_id"] = str(desc["user_id"])  # Convert user_id to string

        return {"descriptions": descriptions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching job descriptions: {str(e)}")
