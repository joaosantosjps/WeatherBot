import os
from pymongo import MongoClient


class MongodbDatabase:
    def __init__(self):
        self.client = MongoClient(f"{os.getenv("MONGODB_HOST")}?authSource=admin")
        self.db = self.client["Weather_Forecast"] 
        
    def collection_create(self):
        collections = self.db.list_collection_names()

        if not "Weather" in collections:
            self.db.create_collection("Weather")
        
        collection = self.db["Weather"]

        return collection
    