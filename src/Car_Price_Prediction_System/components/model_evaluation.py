from Car_Price_Prediction_System import logger
import os
import numpy as np
import pandas as pd
import mlflow
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from Car_Price_Prediction_System.config.configuration import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        logger.info("Loading Testing Data")
        test_df = pd.read_csv(self.config.test_data_file_path)

        X_test = test_df.drop(columns=[self.config.target_column])
        y_test = test_df[self.config.target_column]

        model = {
            "RandomForestRegressor": "RandomForestRegressor.joblib",
            "GradientBoostingRegressor": "GradientBoostingRegressor.joblib",
            "AdaBoostRegressor": "AdaBoostRegressor.joblib",
            "ExtraTreesRegressor": "ExtraTreesRegressor.joblib"
        }

        best_score = float("-inf")
        best_model = None
        best_model_name = None

        mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
        mlflow.set_experiment(self.config.experiment_name)

        for model_name, filename in model.items():
            logger.info(f"Evaluating {model_name}")

            model_path = os.path.join(self.config.model_dir, filename)

            model = joblib.load(model_path)

            predictions = model.predict(X_test)

            r2 = r2_score(y_test, predictions)
            mae = mean_absolute_error(y_test, predictions)
            rmse = np.sqrt(mean_squared_error(y_test, predictions))

            logger.info(f"{model_name} -> R2: {r2:.4f}, MAE: {mae:.4f}, RMSE: {rmse:.4f}")

            with mlflow.start_run(run_name=f"{model_name}_evaluation"):
                mlflow.log_metric("r2_score", r2)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("rmse", rmse)

                if r2 > best_score:
                    best_score = r2
                    best_model = model
                    best_model_name = model_name

            logger.info(f"Best Model: {best_model_name}")
            logger.info(f"Best R2 Score: {best_score}")

            joblib.dump(best_model, self.config.best_model_path)
            logger.info("Best Model Saved Successfully")