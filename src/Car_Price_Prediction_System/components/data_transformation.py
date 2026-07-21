from Car_Price_Prediction_System import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from Car_Price_Prediction_System.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def transform(self):
        logger.info("Loading Dataset")
        data = pd.read_csv(self.config.data_file)

        data.replace({"Fuel_Type": {'Petrol': 0, 'Diesel': 1, 'CNG': 2}}, inplace=True)
        data.replace({"Seller_Type": {'Dealer': 0, 'Individual': 1}}, inplace=True)
        data.replace({"Transmission": {'Manual': 0, 'Automatic': 1}}, inplace=True)
        logger.info("Completed Data Preprocessing")

        X = data.drop(['Car_Name', 'Selling_Price'], axis=1)
        y = data['Selling_Price']

        logger.info("Splitting Dataset")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        train_df = X_train.copy()
        train_df['Selling_Price'] = y_train

        test_df = X_test.copy()
        test_df['Selling_Price'] = y_test

        train_df.to_csv(self.config.train_data_file_path, index=False)
        test_df.to_csv(self.config.test_data_file_path, index=False)
        logger.info("Processed Data Saved Successfully")