from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    bucket_name: str
    object_name: str
    local_data_file: str

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_file: str
    status_file: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_file: str
    train_data_file_path: str
    test_data_file_path: str
    preprocessor_obj_file_path: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_file_path: str
    target_column: str
    mlflow_tracking_uri: str
    experiment_name: str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_file_path: str
    model_dir: Path
    best_model_path: str
    mlflow_tracking_uri: str
    experiment_name: str
    target_column: str