import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.until import save

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix

from dataclasses import dataclass
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout
import keras_tuner as kt



class model_path_config:
    model_path = os.path.join("artifacts", "ann_model.pkl")


class model_trainer:
    def __init__(self):
        self.model_save = model_path_config()

    def initial_data(self, x_train_transform, y_train, x_test_transform, y_test):
        try:
            logging.info("model building start.")
            model =  Sequential()

            model.add(Dense(16, activation="elu", input_dim = 11))
            model.add(Dense(80, activation="relu"))
            model.add(Dense(112, activation="elu"))
            model.add(Dense(1, activation= 'sigmoid'))
            model.compile(optimizer= 'adam',loss= 'binary_crossentropy', metrics=['accuracy'])



            logging.info("model building completed now model training started")
            stop_early = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)

            model.fit(x_train_transform, y_train, epochs = 500, validation_data = (x_test_transform, y_test))

            logging.info("model training complited and now testing started")
            yprob = model.predict(x_test_transform)
            ypred = np.where(yprob>0.5, 1,0)
            accuracy =  accuracy_score(y_test, ypred)
            matrix =  confusion_matrix(y_test, ypred)

            logging.info("model saving started")

            save(
                file_path= self.model_save.model_path,
                obj= model
            )
            logging.info("accuracy and confusion matrix returing")
            return(
                accuracy,
                matrix
            )
            
        except Exception as e:
            raise CustomException(e, sys)



