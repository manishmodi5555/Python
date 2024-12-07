import pyttsx3
import time
text_speech = pyttsx3.init()
wat="please drink water 1 hour is compelete "
def fx():
    time.sleep(1)
    return text_speech.say(wat),text_speech.runAndWait()
print(fx())