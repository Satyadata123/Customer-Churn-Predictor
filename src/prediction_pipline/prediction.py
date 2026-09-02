import pandas as pd
import os
import sys
from src.until import load_data
from src.exception import CustomException
import numpy as np

class pipline:
    def __init__(self , user_data):
        self.user_data = user_data
        
    def predict(self):
        try:
            preproces_file_path = os.path.join("artifacts","transform.pkl")
            model_file_path = os.path.join("artifacts","ann_model.pkl")


            preprocess = load_data(file_path= preproces_file_path)
            model = load_data(file_path= model_file_path)


            data_transform = preprocess.transform(self.user_data)
            yprob = model.predict(data_transform)
            ypred = np.where(yprob>0.5, 1,0)

    
            return (yprob, ypred) 

        except Exception as e:
            raise CustomException(e, sys)


