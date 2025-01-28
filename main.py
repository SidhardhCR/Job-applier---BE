from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext

from fastapi import FastAPI

app = FastAPI()


# MongoDB connection details
MONGO_DETAILS = "mongodb://localhost:27017"  # Update with your MongoDB URI if needed
client = AsyncIOMotorClient(MONGO_DETAILS)
db = client["JobFinder"]  # Replace with your database name
users_collection = db["user_details"]  # Replace with your collection name



@app.get("/")
def read_root():
    return {"Hello": "World"}

# Pydantic model for input validation
class UserSignup(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

@app.post("/signup/")
async def signup(user: UserSignup):
    # Check if the email already exists in MongoDB
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Hash the password before saving it to the database
    hashed_password = hash_password(user.password)
    
    # Convert the Pydantic model to a dictionary and insert into MongoDB
    user_data = user.dict()
    user_data["password"] = hashed_password  # Add the hashed password
    
    # Insert the user data with the hashed password
    result = await users_collection.insert_one(user_data)
    
    return {"message": "User registered successfully", "user_id": str(result.inserted_id)}




# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

# Hash password (used for signup, but kept here for completeness)
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)



@app.post("/login/")
async def login(user: UserLogin):
    # Check if the user exists
    existing_user = await users_collection.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    # Validate the password
    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    return {"message": "Login successful", "user_id": str(existing_user["_id"])}


