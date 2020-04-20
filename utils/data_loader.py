import pandas as pd
import os
import numpy as np
import cv2
from utils import constants as const
import matplotlib.pyplot as plt

class DataLoader:

    def load_data():
        '''
        This function is handling the data loading and pre-processing

        :return: (xtrain, ytrain), (xtest, ytest)
        '''
        print('**** Read data into DAugmentor ****')

        x_train = []
        y_train = []
        x_test = []
        y_test = []

        # setting the path to metadata
        path = const.PATH

        metadata_csv_path = os.path.join(path, const.FILE_METADATA)
        test_img_dir_path = os.path.join(path, const.DIR_TEST)
        train_img_dir_path = os.path.join(path, const.DIR_TRAIN)
        print(metadata_csv_path)

        # setting the path to train data
        x_train_path = os.path.join(path, const.DIR_TRAIN)
        print(x_train_path)

        # setting the path to train data
        x_test_path = os.path.join(path, const.DIR_TEST)

        # reading meta data file as dataframe
        df = pd.read_csv(metadata_csv_path, delimiter=',')

        # dataset format:
        #   image_name
        #   label
        #   data_type

        data_type_row = df["data_type"].tolist()
        image_row = df["image_name"].tolist()
        label_row = df["label"].tolist()

        data_rows = len(data_type_row)

        for row in range(data_rows):
            if (data_type_row[row] == "TRAIN"):
                # setting the path of the current image
                img_path = os.path.join(train_img_dir_path, image_row[row])
                # reading image
                image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                # downscaling image to 28x28
                image = cv2.resize(image, (28, 28))
                x_train.append(image)
                print("Loaded: " + img_path)
                # extracting labels
                y_train.append(label_row[row])

            if (data_type_row[row] == "TEST"):
                # setting the path of the current image
                img_path = os.path.join(test_img_dir_path, image_row[row])
                # reading image
                image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                # downscaling image to 28x28
                image = cv2.resize(image, (28, 28))
                x_test.append(image)
                print("Loaded: " + img_path)
                # extracting labels
                y_test.append(label_row[row])

        xtrain = np.asarray(x_train)
        ytrain = np.asarray(y_train)
        xtest = np.asarray(x_test)
        ytest = np.asarray(y_test)

        print(x_train[0].shape)
        print(x_train[0].shape)

        print(xtrain[0].shape)
        print(x_test[0].shape)

        #(X_train, y_train), (X_test, y_test)
        return (xtrain, ytrain), (xtest, ytest)