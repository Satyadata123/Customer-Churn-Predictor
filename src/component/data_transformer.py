import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.until import save

import pandas as pd
import numpy as np 


from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE



@dataclass
class Data_path_config():
    transform_data_path = os.path.join('artifacts', 'transform.pkl')

class Drop_columns:
    def __init__(self, col):
        self.columns = col

    def fit(self, x, y = None):
        return self

    def transform(self, x):
        return x.drop(self.columns, axis = 1)

class Data_transformation:
    def __init__(self):
        self.data_transform = Data_path_config()

    def get_transformation(self):
        try:
            drop_columns = ['RowNumber','CustomerId', 'Surname']
            one_hot_columns = ['Geography', 'Gender']
            
            preprocesser = ColumnTransformer(
                transformers=[
                    ("cats" , OneHotEncoder(drop= 'first'), one_hot_columns)
                    ],
                    remainder= "passthrough"
                )

            pipeline = Pipeline(
                steps=[
                    ("Drop", Drop_columns(drop_columns)),
                    ("one_hot_encoding",  preprocesser),
                    ("scaler", StandardScaler())
                    ])



            return pipeline

        except Exception as e:
            raise CustomException(e, sys)



    def initial_data_transform(self, x_train, x_test):
        try:

            logging.info("Data loading")
            x_train_data = pd.read_csv(x_train)
            x_test_data = pd.read_csv(x_test)

            preprocessing = self.get_transformation()

            logging.info("data loading completed now seperating the y_train, y_test")
            x_train = x_train_data.drop(columns=['Exited'])
            y_train = x_train_data['Exited']
            

            
            x_test = x_train_data.drop(columns=['Exited'])
            y_test = x_train_data['Exited']
            

            logging.info("data tansfomation are started")
            x_train_transform = preprocessing.fit_transform(x_train)
            x_test_transform = preprocessing.transform(x_test)
            smote = SMOTE(random_state=42)
            X_train_balanced, y_train_balanced = smote.fit_resample(x_train_transform, y_train)

            logging.info("data transfomation complete. transfomation pickle file saving")

            save(
                file_path= self.data_transform.transform_data_path, 
                obj= preprocessing
            )

            logging.info("returning the data , x_train, y_train, x_train, x_test")
            return (
                X_train_balanced,
                y_train_balanced,
                x_test_transform, 
                y_test
            )

        
        except Exception as e:
            raise CustomException(e, sys)