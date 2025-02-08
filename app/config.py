import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client[DB_NAME]

# Access collections from db
users_collection = db[os.getenv("COLLECTION_USER_DETAILS")]
user_job_details = db[os.getenv("COLLECTION_JOB_DETAILS")]
