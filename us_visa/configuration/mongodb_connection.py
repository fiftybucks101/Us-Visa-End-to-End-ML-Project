import os
import sys
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY, COLLECTION_NAME
import pymongo
import certifi
from us_visa.logger import logging
from us_visa.exception import USvisaException
from dotenv import load_dotenv

ca = certifi.where()

class MongoDBClient:
    '''
    Class Name: export data into Data Store
    Description: This method imports the dataframe from mongobd as dataframe
    Output: connection to mongodb database
    '''

    client = None
    load_dotenv('project.env')

    def __init__(self, database_name=DATABASE_NAME, collection_name=COLLECTION_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")

        except Exception as e:
            raise USvisaException(e,sys)