from pathlib import Path
import logging

project_name = "Car_Price_Prediction_System"

logging.basicConfig(
    level=logging.INFO, 
    format="[%(asctime)s] : %(levelname)s : %(message)s"
)

list_of_files = [
    ".github/workflows/.gitkeep",
    "config/config.yaml",
    "config/schema.yaml",
    "config/params.yaml",
    f"src/{project_name}/__init__.py",
    f"notebooks/EDA.ipynb",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipelines/__init__.py",
    "requirements.txt",
    "setup.py",
    "main.py",
    "streamlit_app.py",
    "Dockerfile",
    "Makefile",
    ".gitignore",
    ".env"
]

def create_project_structure(files: list[str]) -> None:
    for file in files:
        filepath = Path(file)

        try:
            filepath.parent.mkdir(parents=True, exist_ok=True)
            if not filepath.exists():
                filepath.touch(exist_ok=True)
                logging.info(f"Created file: {filepath}")
            else:
                logging.info(f"Already exists: {filepath}")
        except Exception as e:
            raise e
        
def main():
    create_project_structure(list_of_files)


if __name__ == "__main__":
    main()