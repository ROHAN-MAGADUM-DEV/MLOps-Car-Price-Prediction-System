from Car_Price_Prediction_System.config.configuration import ConfigurationManager
from Car_Price_Prediction_System.components.data_validation import DataValidation

class DataValidationPipeline:
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()