#module is pyttxs3 version 2.71
#sapi5 is a voci API BY MICROSOFT
#pyttsx3, version == 2.71
import pyttsx3
from pyttsx3 import engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
engine.setProperty("rate", 180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello sir , My name is Monday, How can I help you.")



