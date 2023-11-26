import json
from pymongo import MongoClient 
from pydantic import BaseModel
import os
import logging
class DatabaseOps():
    client = None
    db = "SWG"
    collection = "Rules"

    @classmethod
    def connect(cls):
        cls.connection_string = os.getenv("MONGO_CONNECTION_STRING")
        if cls.client is None:
            logging.info("Connecting to MongoDB")
            cls.client = MongoClient(cls.connection_string)

        else:
            logging.info("Already connected to MongoDB")    

    @classmethod
    def save_to_mongodb(cls,rules: BaseModel,question:str):
        
        cls.connect()
        # Select the database and collection
        db = cls.client[cls.db]
        collection = db[cls.collection]

        # Serialize Pydantic model to JSON, then load it as a dictionary
        rules_dict = json.loads(rules.model_dump_json())
        rules_dict["question"]=question

        # Insert the data into MongoDB
        collection.insert_one(rules_dict)

        return rules_dict['rules']