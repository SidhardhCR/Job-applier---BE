from motor.motor_asyncio import AsyncIOMotorClient
import os

class Database:
    def __init__(self, uri: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client["JobFinder"]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

# Initialize DB connection
db = Database(os.getenv("MONGO_DETAILS"))


