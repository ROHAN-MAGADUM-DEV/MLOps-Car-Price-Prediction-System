import os
from Car_Price_Prediction_System import logger
import pandas as pd
import joblib
from sklearn.ensemble import (RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, ExtraTreesRegressor)
import mlflow
from sklearn.model_selection import GridSearchCV
from Car_Price_Prediction_System.config.configuration import ModelTrainerConfig
from Car_Price_Prediction_System.utils.common import read_yaml
from Car_Price_Prediction_System.constants import *

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        self.params = read_yaml(Params_Filepath)

    def train(self):
        logger.info("Loading Training Dataset")
        train_df = pd.read_csv(self.config.train_data_file_path)

        X_train = train_df.drop(columns=[self.config.target_column])
        y_train = train_df[self.config.target_column]

        models = {
            "RandomForestRegressor": RandomForestRegressor(),
            "GradientBoostingRegressor": GradientBoostingRegressor(),
            "AdaBoostRegressor": AdaBoostRegressor(),
            "ExtraTreesRegressor": ExtraTreesRegressor()
        }

        mlflow.set_tracking_uri(self.config.mlflow_tracking_uri)
        mlflow.set_experiment(self.config.experiment_name)

        for model_name, model in models.items():
            logger.info(f"Training {model_name}")
            grid_search = GridSearchCV(
                estimator=model,
                param_grid=dict(self.params[model_name]),
                scoring="r2",
                cv=5,
                n_jobs=-1
            )
            logger.info(self.params[model_name])

            with mlflow.start_run(run_name=model_name):
                grid_search.fit(X_train, y_train)

                score = grid_search.best_score_
                model = grid_search.best_estimator_

                logger.info(f"{model_name} CV Score : {score}")

                mlflow.log_params(grid_search.best_params_)
                mlflow.log_metric("cv_r2_score", score)

                mlflow.sklearn.log_model(sk_model=model, name="model")

                local_model_path = os.path.join(self.config.root_dir, f"{model_name}.joblib")

                joblib.dump(model, local_model_path)
                logger.info(f"{model_name} Saved successfully")