from tensorflow import keras
import numpy as np
from scipy.io.wavfile import read
import os

def get_data():
    '''
    gives data to build model
    '''

    safe_dir = os.getcwd() + "/data/safe/" 
    shot_dir = os.getcwd() + "/data/shot/" 

    

    # GET TRAINING DATA
    train_audio = []
    for i in range(1, 56):
        audio = read(safe_dir + "save_{}.wav".format(i))[1]
        train_audio.append(audio)
    train_labels = [False] * 55

    for i in range(1, 26):
        audio = read(shot_dir + "shot_{}.wav".format(i))[1]
        train_audio.append(audio)
    train_labels += [True] * 25

    # GET TESTING DATA
    test_audio = []
    for i in range(56, 70):
        audio = read(safe_dir + "save_{}.wav".format(i))[1]
        test_audio.append(audio)
    test_labels = [False] * 14

    for i in range(26, 32):
        audio = read(shot_dir + "shot_{}.wav".format(i))[1]
        test_audio.append(audio)
    test_labels += [True] * 6

    train_audio = np.asarray(train_audio)
    train_labels = np.asarray(train_labels)
    test_audio = np.asarray(test_audio)
    test_labels = np.asarray(test_labels)

    return (train_audio, train_labels), (test_audio, test_labels)

def build_model():
    '''
    builds and returns ML model
    '''

    (train_data, train_labels), (test_data, test_labels) = get_data()

    train_data = train_data
    test_data = test_data
    
    model = keras.Sequential([
        keras.layers.Flatten(input_shape = (132300, 2)),
        keras.layers.Dense(100, activation = "relu"),
        keras.layers.Dense(20, activation = "softmax"),
        keras.layers.Dense(5, activation = "relu")
    ])

    model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

    model.fit(train_data, train_labels, epochs = 20)

    test_loss, test_acc = model.evaluate(test_data, test_labels)

    print("test acc: {}".format(test_acc))

    return model
