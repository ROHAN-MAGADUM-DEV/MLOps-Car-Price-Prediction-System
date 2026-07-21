from Car_Price_Prediction_System.constants import *
from Car_Price_Prediction_System.utils.common import read_yaml, create_directories
from Car_Price_Prediction_System.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self, config_filepath=Config_Filepath, params_filepath=Params_Filepath, schema_filepath=Schema_Filepath):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            bucket_name=config.bucket_name,
            object_name=config.object_name,
            local_data_file=config.local_data_file
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            data_file = config.data_file,
            status_file = config.status_file,
            all_schema = schema
        )

        return data_validation_config