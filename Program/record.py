import settings
import sounddevice as sd
from scipy.io.wavfile import write

fs = settings.fs
seconds = settings.seconds
channels = settings.channels

def record_sample():

    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    
    try:
		myrecording = sd.rec(int(fs * seconds), fs, channels)
        sd.wait()  # Wait until recording is finished
	except:
		settings.channels = 1
		myrecording = sd.rec(int(fs * seconds), fs, channels=1)
        sd.wait()  # Wait until recording is finished
    
    write("test.wav", 44100, myrecording)

	sd.wait()  # Wait until recording is finished
	return myrecording

def record_extended(myrecording):
    myrecording2 = sd.playrec(myrecording, fs, channels)
    sd.wait()