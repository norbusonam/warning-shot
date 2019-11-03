import settings
import audio_model
import record
import time
import sounddevice as sd
import numpy as np


def status_operations(status, model):
    
    while (status == "normal"):
        # *not implementing yet* Get overlapping recordings - 2 second overlap
        recording = record.record_sample()

        recording = np.asarray([recording])
        prediction = model.predict(recording)
        shot = np.argmax(prediction[0])
        if shot:
            status = "recording"
            break

        # model = keras.Sequ

       # if (model.evaluate(recording))
        
        # Keras.layers.Flatten
            #break
    if status == "recording":
        print("Gunshot detected.")
        print("Current Status: Recording")
        myrecording = sd.rec(int(duration * fs), fs, channels)
        sd.wait()
        myrecording = sd.playrec(myrecording, fs, channels)
        print("Playing last ", seconds, " seconds of audio...")
        user_update_status = input("Enter 1234 to confirm valid threat or enter anything else to clear alarm (false detection): ")
        if (user_update_status != "1234"):
            print("Alarm successfully cleared. Resuming normal status...")
            status = "normal"

    # Threat detected and confirmed. Continuously stream audio clips.
    while (status == "recording"):
        record.record_extended(myrecording)
        


if __name__ == "__main__":

    status = "normal" # initialize to normal operation (no emergency)
    model = audio_model.build_model()

    status_operations(status, model)