import os
import boto3
from dotenv import load_dotenv
from Car_Price_Prediction_System.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        load_dotenv()

        access_key = os.getenv("AWS_ACCESS_KEY_ID")
        secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        region = os.getenv("AWS_DEFAULT_REGION")

        s3 = boto3.client(
            "s3",
            aws_access_key_id = access_key,
            aws_secret_access_key = secret_key,
            region_name = region
        )

        s3.download_file(
            Bucket="car-price-prediction-system",
            Key="car_data.csv",
            Filename="artifacts/data_ingestion/car_data.csv"
        )