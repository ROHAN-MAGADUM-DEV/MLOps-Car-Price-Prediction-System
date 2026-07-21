from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    bucket_name: str
    object_name: str
    local_data_file: str