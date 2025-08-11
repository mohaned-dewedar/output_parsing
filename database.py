import json
from pymongo import MongoClient 
from pydantic import BaseModel
import os
import logging
import bson
from typing import List
from datetime import datetime

class DatabaseOps():
    """
    Class to handle all database operations
    """
    client = None
    db = "YouDBName"
    collection = "YourCollectionName"

    @classmethod
    def connect(cls):
        """
        Connect to MongoDB Atlas
        """
        cls.connection_string = os.getenv("MONGO_CONNECTION_STRING")
        if cls.client is None:
            logging.info("Connecting to MongoDB")
            cls.client = MongoClient(cls.connection_string)

        else:
            logging.info("Already connected to MongoDB")    

    @classmethod
    def save_to_mongodb(cls,rules: List[BaseModel], question:str,model_name:str):
        """
        Save the rules to MongoDB
        args: 
            rules: List of rules
            question: Question for which the rules are generated
            model_name: Name of the OpenAI model

        returns: 
            rules: List of rules as a dictionary
            message_id: Unique message ID        
        """
        
        cls.connect()
        # Select the database and collection
        db = cls.client[cls.db]
        collection = db[cls.collection]

        # Generate a unique message ID 
        message_id = str(bson.ObjectId())   
        rules_list = rules.rules
        #Iterate over each rule and save it individually with the question and message ID
        for i,rule in enumerate(rules_list):

            rule_dict= {'date': datetime.utcnow(),
                        'question': question,
                        'message_id': message_id,
                        'rule_id': i+1,
                        'model_name': model_name}
                         
            # Serialize individual rule to JSON, then load it as a dictionary
            rule_dict.update(json.loads(rule.model_dump_json()))
            

            # Insert the individual rule data into MongoDB
            collection.insert_one(rule_dict)
        

        return json.loads(rules.model_dump_json()) , message_id