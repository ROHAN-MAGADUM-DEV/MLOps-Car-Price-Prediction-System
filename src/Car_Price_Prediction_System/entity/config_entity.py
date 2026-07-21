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