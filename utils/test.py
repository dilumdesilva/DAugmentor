import os
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt
from utils import constants as const

path = const.PATH
metadata_csv_path = os.path.join(path, const.FILE_METADATA)
test_img_dir_path = os.path.join(path, const.DIR_TEST)
train_img_dir_path = os.path.join(path, const.DIR_TRAIN)

df = pd.read_csv(metadata_csv_path, delimiter=',')

data_type_row = df["data_type"].tolist()
image_row = df["image_name"].tolist()
label_row = df["label"].tolist()

data_rows = len(data_type_row)

x_train = []
y_train = []
x_test = []
y_test = []

for row in range(data_rows):
    if (data_type_row[row] == "TRAIN"):
        # setting the path of the current image
        img_path = os.path.join(train_img_dir_path, image_row[row])
        # reading image
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        # downscaling image to 256x256
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
        # downscaling image to 256x256
        image = cv2.resize(image, (28, 28))
        x_test.append(image)
        print("Loaded: " + img_path)
        # extracting labels
        y_test.append(label_row[row])

#x_train = x_train.reshape(5286, 28, 28, 1)
#x_test = x_train.reshape(624, 28, 28, 1)

print(len(x_train))
print(len(x_test))

xtrain = np.asarray(x_train)
#xtrain = xtrain.reshape(28, 28, 1)
ytrain = np.asarray(y_train)

xtest = np.asarray(x_test)
#xtest = xtest.reshape(28, 28, 1)
ytest = np.asarray(y_test)

print(x_train[0].shape)
print(x_train[0].shape)

print(xtrain[0].shape)
print(x_test[0].shape)

i = x_train[100]
plt.imshow(i)
plt.show()

print("done")
