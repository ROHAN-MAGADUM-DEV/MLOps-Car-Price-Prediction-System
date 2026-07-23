from Car_Price_Prediction_System.constants import *
from Car_Price_Prediction_System.utils.common import read_yaml, create_directories
from Car_Price_Prediction_System.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig

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

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_file = config.data_file,
            train_data_file_path = config.train_data_file_path,
            test_data_file_path = config.test_data_file_path,
            preprocessor_obj_file_path = config.preprocessor_obj_file_path
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
    
        create_directories([config.root_dir])
    
        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_file_path = config.train_data_file_path,
            target_column=schema.name,
            mlflow_tracking_uri=config.mlflow_tracking_uri,
            experiment_name=config.experiment_name
        )
    
        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
    
        create_directories([config.root_dir])
    
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_file_path=config.test_data_file_path,
            model_dir=config.model_dir,
            best_model_path=config.best_model_path,
            mlflow_tracking_uri=config.mlflow_tracking_uri,
            experiment_name=config.experiment_name,
            target_column=schema.name
        )
    
        return model_evaluation_config