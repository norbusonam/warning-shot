import sounddevice as sd
from scipy.io.wavfile import write

def record_sample():

    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write("test.wav", 44100, myrecording)

    return myrecording 

def record_extended(myrecording):
    fs = 44100 # Sample rate
    myrecording2 = sd.playrec(myrecording, fs, channels = 2)
    sd.wait()