from us_visa.configuration.mongodb_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME,COLLECTION_NAME
from us_visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np
from us_visa.logger import logging


class USvisaData:
    '''
    This class help to export entire mongo db record as pandas dataframe
    '''

    def __init__(self):
        try:
            logging.info('Fetching data from mongodb initated')
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e,sys)
        
    def export_collection_as_dataframe(self,collection_name:str,database_name:str) -> pd.DataFrame:
        try:
            '''
            export entire collection as dataframe:
            return pd.DataFrame of collection
            '''

            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                database = self.mongo_client.client[database_name]
                collection = database[collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e,sys)