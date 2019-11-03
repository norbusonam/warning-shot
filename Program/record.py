import settings
import sounddevice as sd
from scipy.io.wavfile import write

fs = settings.fs
seconds = settings.seconds
channels = settings.channels

def record_sample():

    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    
<<<<<<< HEAD
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
=======
    try:
        myrecording = sd.rec(int(fs * seconds), fs, channels)
        sd.wait()  # Wait until recording is finished
    except:
        settings.channels = 1
        myrecording = sd.rec(int(fs * seconds), fs, channels=1)
        sd.wait()  # Wait until recording is finished
    
    write("test.wav", 44100, myrecording)
>>>>>>> 630329d92d30a694166fb4179a221c029c0b012f

    sd.wait()  # Wait until recording is finished
    return myrecording

def record_extended(myrecording):
<<<<<<< HEAD
    fs = 44100 # Sample rate
    myrecording2 = sd.playrec(myrecording, fs, channels = 1)
=======
    myrecording2 = sd.playrec(myrecording, fs, channels)
>>>>>>> 630329d92d30a694166fb4179a221c029c0b012f
    sd.wait()