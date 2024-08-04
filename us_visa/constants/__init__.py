import os
from datetime import date

DATABASE_NAME = "US_VISA"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"
FILE_NAME: str = "us_visa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION variable name
"""

DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "Data Ingestion"
DATA_INGESTION_DATA_STORE_DIR: str  = "Data Store"
DATA_INGESTION_INGESTED_DATA_DIR: str = "Ingested Data"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2