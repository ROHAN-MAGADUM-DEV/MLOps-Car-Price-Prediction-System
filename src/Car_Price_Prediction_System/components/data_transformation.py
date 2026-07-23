from Car_Price_Prediction_System import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler ,OneHotEncoder
import joblib
from Car_Price_Prediction_System.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def create_preprocessor(self, X_train):
        logger.info("Creating preprocessor")

        categorical_cols = X_train.select_dtypes(include="object").columns
        numerical_cols = X_train.select_dtypes(include="number").columns

        preprocessor = ColumnTransformer([
            ("cat", OneHotEncoder(handle_unknown="ignore", drop="first"), categorical_cols),
            ("num", StandardScaler(), numerical_cols)
        ])

        preprocessor.fit(X_train)

        joblib.dump(preprocessor, self.config.preprocessor_obj_file_path)
        logger.info("Preprocessor saved")

        return preprocessor

    def save_train_test_data(self):
        logger.info("Loading dataset")

        data = pd.read_csv(self.config.data_file)

        X = data.drop(columns=["Car_Name", "Selling_Price"])
        y = data["Selling_Price"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        preprocessor = self.create_preprocessor(X_train)

        train_df = pd.DataFrame(preprocessor.transform(X_train))
        train_df["Selling_Price"] = y_train.reset_index(drop=True)

        test_df = pd.DataFrame(preprocessor.transform(X_test))
        test_df["Selling_Price"] = y_test.reset_index(drop=True)

        train_df.to_csv(self.config.train_data_file_path, index=False)
        test_df.to_csv(self.config.test_data_file_path, index=False)

        logger.info("Train/Test data saved successfully")