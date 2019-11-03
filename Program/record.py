import settings
import tensorflow
from tensorflow import keras
import os
import numpy as np
import matplotlib.pyplot as plt
import time
import sounddevice as sd
from scipy.io.wavfile import write

fs = settings.fs
seconds = settings.seconds
channels = settings.channels

def record_sample():
	try:
		myrecording = sd.rec(int(fs * seconds), fs, channels)
	except:
		settings.channels = 1
		myrecording = sd.rec(int(fs * seconds), fs, channels=1)


	sd.wait()  # Wait until recording is finished
	return myrecording

def record_extended(myrecording):
    myrecording2 = sd.playrec(myrecording, fs, channels)
    sd.wait()