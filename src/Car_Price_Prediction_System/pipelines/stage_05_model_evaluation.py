from Car_Price_Prediction_System.config.configuration import ConfigurationManager
from Car_Price_Prediction_System.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()