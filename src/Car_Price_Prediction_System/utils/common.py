from pathlib import Path
import logging
import yaml
from box import ConfigBox
import os

def read_yaml(filepath: Path) -> ConfigBox:
    try:
        with filepath.open("r") as file:
            content = yaml.safe_load(file)
            logging.info(f"Created File: {file}")
        return ConfigBox(content)
    except Exception as e:
        raise e

def create_directories(directories: list, verbose: bool = True) -> None:
    try:
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
            if verbose:
                logging.info(f"Created Directory: {directory}")
    except Exception as e:
        raise e