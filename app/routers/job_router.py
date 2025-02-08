from fastapi import APIRouter, HTTPException
from app.scrape import scrape_jobs
from app.config import users_collection, user_job_details
from bson.objectid import ObjectId
router = APIRouter()


@router.get("/scrape-jobs/{user_id}")
async def get_scraped_jobs(user_id: str):

    print("Scraping jobs...")
    jobs = scrape_jobs()
    skills = handle_scrape_jobs(jobs, user_id)
    print(skills)


def handle_scrape_jobs(jobs, user_id):
    print(user_id)
    print(ObjectId(user_id))
    # Assuming you have a user_id to query
    user = user_job_details.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    skills = user.get("skills", [])
    return skills
