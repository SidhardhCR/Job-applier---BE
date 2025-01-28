from app.services import hash_password, verify_password
from app.models import UserSignup
from fastapi import HTTPException

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
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "user_id": str(existing_user["_id"])}
