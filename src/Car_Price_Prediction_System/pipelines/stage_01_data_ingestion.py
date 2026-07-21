from Car_Price_Prediction_System.config.configuration import ConfigurationManager
from Car_Price_Prediction_System.components.data_ingestion import DataIngestion

class DataIngestionPipeline:
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()