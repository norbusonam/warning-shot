import audio_model
import alert_system
import record
import numpy as np
import sounddevice as sd

def status_operations(status, model):
    
    while (status == "normal"):
        # *not implementing yet* Get overlapping recordings - 2 second overlap
        recording = record.record_sample()
        recording = np.asarray([recording])
        prediction = model.predict(recording)[0][0]
        if prediction == 1:
            status = "recording"
            break
        else:
            print("No Clap")

    if status == "recording":
        print("Gunshot detected.")
        print("Sending allerts...")
        alert_system.send_message("West Wing,Room 1C13")
        print("Current Status: Recording")
        seconds = 10
        fs = 44100
        myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels=2)
        sd.wait()
        myrecording = sd.playrec(myrecording, fs, channels=1)
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