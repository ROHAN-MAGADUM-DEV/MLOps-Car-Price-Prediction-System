from Car_Price_Prediction_System.config.configuration import ConfigurationManager
from Car_Price_Prediction_System.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()