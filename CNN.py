import os
import os.path
import numpy as np
import pandas as pd

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K
from tensorflow.keras import models, layers
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model



def prediction(video_file):
    filename, _ = os.path.splitext(video_file)
    path_folder = "/Users/justusweissmuller/Desktop/spiced/FinalProject/finalcode/"
    path = path_folder+filename+"-opencv/"
    new_path_folder = "/Users/justusweissmuller/Desktop/spiced/FinalProject/finalcode/"
    new_path = new_path_folder+filename+"-img/"

    Z =[]
    classes = [filename+"-img/"] #name of the folders, where screenshots are stored in

    for i, target in enumerate(classes):
        files = os.listdir(new_path_folder+target)

        for file in files:
            # load the image
            img = load_img(new_path_folder+target+'/'+file)

            # convert it to an array
            img_array = img_to_array(img)

            # append the array to Z
            Z.append(img_array)

    Y = np.array(Z)
    #print(f'Y input:{Y.shape}')

    model = load_model("model6.h5")
    ypred = model.predict(Y)
    return ypred



def img_per_track (ypred):

    asphalt_track_field = []
    asphalt_track_forest = []
    dirt_track_field = []
    dirt_track_forest = []

    y_pred_labels= np.argmax(ypred, axis=1)


    for i in y_pred_labels:
        if i == 0:
             asphalt_track_forest.append(i)
        elif i == 1:
            asphalt_track_field.append(i)
        elif i == 2:
            dirt_track_field.append(i)
        elif i == 3:
            dirt_track_forest.append(i)

    return asphalt_track_field, asphalt_track_forest, dirt_track_field, dirt_track_forest
