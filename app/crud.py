from app.services import hash_password, verify_password
from app.models import UserSignup
from fastapi import HTTPException
from pymongo import UpdateOne


async def signup_user(user: UserSignup, users_collection):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_password(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password

    result = await users_collection.insert_one(user_data)
    return str(result.inserted_id)


async def login_user(user: UserSignup, users_collection):
    existing_user = await users_collection.find_one({"email": user.email})
    USER_ID = str(existing_user["_id"])
    if not existing_user:
        raise HTTPException(
            status_code=400, detail="Invalid email or password")

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(
            status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user_id": str(existing_user["_id"])}


async def user_job_description(data, user_job_details):
    """Insert or update user job description with a skillsUpdated flag."""
    
    # Define filter condition (Assuming user_id is unique for job descriptions)
    filter_condition = {"user_id": data.user_id}

    # Fetch existing data (if any)
    existing_record = await user_job_details.find_one(filter_condition)

    # Extract existing skills if record exists
    existing_skills = existing_record.get("skills", []) if existing_record else []

    # Determine if skills have changed
    skillsUpdated = set(existing_skills) != set(data.skills)

    # Define update operation
    update_operation = {
        "$set": data.dict()  # Update fields if already exists
    }

    # Perform upsert (update if exists, insert if not)
    response = await user_job_details.update_one(filter_condition, update_operation, upsert=True)

    if response.upserted_id:
        return {"message": "Job description added successfully", "skillsUpdated": True}
    else:
        return {"message": "Job description updated successfully", "skillsUpdated": skillsUpdated}


# async def user_job_description(data, user_job_details):
#     response = await user_job_details.insert_one(data.dict())
#     return {"message": "Job description submitted successfully"}
