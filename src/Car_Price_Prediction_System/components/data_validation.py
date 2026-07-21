import pandas as pd
from Car_Price_Prediction_System import logger
from Car_Price_Prediction_System.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    
    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.data_file)
            csv_columns = set(data.columns)
            schema_columns = set(self.config.all_schema)
            validation_status = csv_columns == schema_columns

            with open(self.config.status_file, "w") as file:
                file.write(f"Validation Status: {validation_status}")

            logger.info(f"Validation Status Saved To: {self.config.status_file}")
        except Exception as e:
            raise e