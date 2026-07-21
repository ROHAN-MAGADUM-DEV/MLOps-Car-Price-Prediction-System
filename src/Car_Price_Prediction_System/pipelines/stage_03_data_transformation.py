
from Car_Price_Prediction_System.config.configuration import ConfigurationManager
from Car_Price_Prediction_System.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.transform()