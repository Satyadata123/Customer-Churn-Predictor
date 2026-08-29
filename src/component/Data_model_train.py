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
    model_path = os.path.join("artifacts", "model.pkl")


class model_trainer:
    def __init__(self):
        self.model_save = model_path_config()

    def initial_data(self, x_train_transform, y_train, x_test_transform, y_test):
        try:
            logging.info("model building start.")
            model =  Sequential()

            model.add(Dense(16, activation="elu", input_dim = x_train_transform.shape[1]))
            model.add(Dense(80, activation="relu"))
            model.add(Dense(112, activation="elu"))
            model.add(Dense(1, activation= 'sigmoid'))
            model.compile(optimizer= 'adam',loss= 'binary_crossentropy', metrics=['accuracy'])


            # def model_builder(hp):
            #     model = keras.Sequential()
            #     count = 0

            #     for i in range(hp.Int('num_layers', min_value = 1, max_value = 10)):
            #         if count == 0:
            #             unite = hp.Int('num_node' + str(i), min_value= 8, max_value = 128, step = 8)
            #             activation_fun = hp.Choice('activation_' + str(i), values = ['relu', 'tanh', 'selu', 'elu'])
            #             model.add(
            #             Dense(units=unite,
            #                 activation= activation_fun, 
            #                 input_dim = x_train_transform.shape[1]
            #                 )
            #             )

            #         else:
            #             unite = hp.Int('num_node' + str(i), min_value= 8, max_value = 128, step = 8)
            #             activation_fun = hp.Choice('activation_' + str(i), values = ['relu', 'tanh', 'selu', 'elu'])
            #             model.add(
            #             Dense(units=unite,
            #                 activation= activation_fun
            #                 )
            #             )

            #         count+= 1
      

            #     model.add(Dense(1, activation= 'sigmoid'))
            #     model.compile(optimizer= hp.Choice('optimizer', values = ['adam', 'rmsprop', 'sgd', 'nadam', 'adadelta']),
            #     loss= 'binary_crossentropy',
            #     metrics=['accuracy'])

            #     return model


            # tuner = kt.RandomSearch(model_builder,
            #          objective='val_accuracy',
            #          max_trials=5,
                   
            #          directory='my_dir',
            #          project_name='intro_to_kt')

            # tuner.search(x_train_transform, y_train, epochs=5, validation_data = (x_test_transform, y_test))

            # model =tuner.get_best_models(num_models=1)[0]
            # stop_early = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)
            # model.fit(x_train_transform, y_train, epochs = 200, initial_epoch = 6, validation_data = (x_test_transform, y_test), callbacks = stop_early)



            logging.info("model building completed now model training started")
            stop_early = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)

            model.fit(x_train_transform, y_train, epochs = 500, callbacks = stop_early)

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



