from fastapi import APIRouter, HTTPException
from app.scrape import scrape_jobs
from app.config import users_collection, user_job_details, matching_Jobs
from bson.objectid import ObjectId
from dotenv import load_dotenv

import os
import shutil
from fastapi import APIRouter, UploadFile, File
from pymongo import MongoClient


router = APIRouter()

load_dotenv()
async def scrape_and_process_jobs(userData: dict):
    """Scrapes jobs and processes them asynchronously."""
    try:
        print("✅ scrape_and_process_jobs function started!")
        jobs = scrape_jobs()
        print(f"✅ Scraped {len(jobs['jobs'])} jobs!")

        # ✅ Use `await` since `filter_jobs_by_skills` is async
        await filter_jobs_by_skills(jobs["jobs"], userData["skills"], userData["user_id"])

    except Exception as e:
        print(f"❌ Error in scrape_and_process_jobs: {str(e)}")

async def filter_jobs_by_skills(jobs, user_skills, user_id):
    """Filters jobs and saves them to MongoDB asynchronously."""
    user_skills_set = set(skill.strip().lower() for skill in user_skills[0].split(","))  
    filtered_jobs = []

    for job in jobs:
        job_skills_set = set(skill.strip().lower() for skill in job["skills"].split(","))  
        if user_skills_set & job_skills_set:  
            filtered_jobs.append(job)

    if not filtered_jobs:
        print(f"⚠️ No matching jobs found for user: {user_id}")
        return []

    job_entry = {
        "user_id": ObjectId(user_id),
        "matched_jobs": filtered_jobs
    }

    print("✅ Prepared job_entry for insertion")

    # ✅ Use `await` for async MongoDB insert
    try:
        result = await matching_Jobs.insert_one(job_entry)
        print(f"✅ Data inserted successfully with ID {result.inserted_id}")
    except Exception as db_error:
        print(f"❌ Database insertion error: {str(db_error)}")

    return filtered_jobs

@router.post("/scrape-jobs/")
async def get_scraped_jobs(userData: dict):
    """Triggers job scraping and processing asynchronously."""
    await scrape_and_process_jobs(userData)
    return {"message": "Scraping and processing completed!"}

@router.get("/getMatched-jobs/")
async def get_matched_jobs():
    """Fetches all matched jobs from the database."""
    try:
        jobs = await matching_Jobs.find().to_list(None)  # Get all jobs
        
        if not jobs:
            return {"message": "No matched jobs found."}
        
        # Convert ObjectId fields to string for JSON serialization
        for job in jobs:
            job["_id"] = str(job["_id"])  # Convert _id
            job["user_id"] = str(job["user_id"])  # Convert user_id
        
        return {"matched_jobs": jobs}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching matched jobs: {str(e)}")
    
    
    
from fastapi import APIRouter, UploadFile, File
import gridfs
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")  # Change if needed
db = client[os.getenv("DB_NAME")]  # Replace with your database name
fs = gridfs.GridFS(db, collection="cvCollection")  

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """ Uploads a PDF file directly to MongoDB GridFS. """
    print("Uploading file to MongoDB...")

    # Read file content as binary
    file_data = await file.read()

    # Upload to GridFS
    file_id = fs.put(file_data, filename=file.filename, content_type=file.content_type)

    return {
        "message": "PDF uploaded successfully!",
        "mongo_file_id": str(file_id),
        "filename": file.filename
    }
