import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from us_visa.entity.config_entity import DataIngestionConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.data_access.dict_to_df import USvisaData


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        '''
        param data_ingestion_config: configuration for data ingestion
        '''

        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise USvisaException(e,sys)

    def export_data_into_data_store(self) -> DataFrame:
        '''
        Method Name: export_data_into_data_store
        Description: This method exports data from mongodb to csv file
        Output: data is returned as artifact of data ingestion components
        '''

        try:
            logging.info("Exporting data from mongodb")
            usvisa_data = USvisaData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name,database_name=self.data_ingestion_config.database_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            data_store_file_path = self.data_ingestion_config.data_store_file_path
            dir_path = os.path.dirname(data_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into Data Store file path: {data_store_file_path}")
            dataframe.to_csv(data_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise USvisaException(e,sys)

    def split_data_as_train_test(self,dataframe: DataFrame) -> None:
        '''
        Description: This method splits the dataframe into train set and test set based on split ratio
        Output: Folder is created in artificate inside data ingestion
        '''

        try:
            train_set, test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_data_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info(f"Exporting train and test file path")
            train_set.to_csv(self.data_ingestion_config.training_data_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_data_file_path,index=False,header=True)

            logging.info(f"Exported train and test file")

        except Exception as e:
            raise USvisaException(e,sys)
        
    def initiate_data_ingestion(self) :
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline 
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_data_store()

            logging.info("Got the data from mongodb")

            self.split_data_as_train_test(dataframe)

            logging.info("Performed train test split on the dataset")

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )

        except Exception as e:
            raise USvisaException(e,sys)