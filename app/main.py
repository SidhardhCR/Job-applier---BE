from dotenv import load_dotenv
import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure
from fastapi.middleware.cors import CORSMiddleware
from app.routers.user_routes import router as user_router




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (you can restrict to specific domains)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_USER_DETAILS = os.getenv("COLLECTION_USER_DETAILS")



# Ensure all required variables are loaded
if not MONGO_DETAILS:
    raise ValueError("MONGO_DETAILS is not set correctly")
if not DB_NAME:
    raise ValueError("DB_NAME is not set correctly")
if not COLLECTION_USER_DETAILS:
    raise ValueError("COLLECTION_USER_DETAILS is not set correctly")


# Include the routes
app.include_router(user_router)
# app.include_router(job_routes.router)

