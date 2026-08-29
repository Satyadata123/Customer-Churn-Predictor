import pandas as pd
import os
import sys
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.component.data_transformer import Data_transformation
from src.component.Data_model_train import model_trainer
from sklearn.model_selection import train_test_split

@dataclass
class Data_ingestion_config():
    train_path = os.path.join("artifacts", "train.csv")
    test_path = os.path.join("artifacts", "test.csv")
    raw_path = os.path.join("artifacts", "raw.csv")


class Data_ingestion():
    def __init__(self):
        self.ingestion_path = Data_ingestion_config()


    def ingestion_data_config(self):
        logging.info("Data is loading")
        try:
            data = pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\churn_prediction\Data\Churn_Modelling.xls")

            
            logging.info("Folder Creation or Check Folder path")
            os.makedirs(os.path.dirname(self.ingestion_path.test_path),  exist_ok= True)

            logging.info("raw data saving")
            # raw data
            logging.info("Raw data storying in artifacts Folder ")
            data.to_csv(self.ingestion_path.raw_path, index= False, header= True )

            logging.info("Train test splite")
            x_train, x_test = train_test_split(data, test_size=0.2, random_state=42)

            logging.info("Train data saveing")
            # train_data
            logging.info("Training Data storing in artifacts folder")
            x_train.to_csv(self.ingestion_path.train_path, index = False, header = True)

            logging.info("Test data saveing")
            # x_test data
            logging.info("Testing Data storing in astifacts Folder")
            x_test.to_csv(self.ingestion_path.test_path, index = False, header = True)

            logging.info("Train Test data return")
            return (
            self.ingestion_path.train_path,
            self.ingestion_path.test_path
            )


        except Exception as e:
            raise CustomException(e, sys)

    



if "__main__" == __name__:

    obj = Data_ingestion()

    x_train, x_test = obj.ingestion_data_config()

    preprocess_obj = Data_transformation()

    x_train_transform,y_train, x_test_transform, y_test =  preprocess_obj.initial_data_transform(x_train, x_test)

    model = model_trainer()
    accuracy, matrix = model.initial_data(x_train_transform,y_train, x_test_transform, y_test)
    print("accuracy :- ",accuracy)
    print("confusion_matrix :-\n", matrix)
    




        

