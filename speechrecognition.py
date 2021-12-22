import speech_recognition as sr
from text_to_speech import speak

def takecommand():
    a = [0]
    while a[0] == 0 :
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #speak("Sir, You can start to talk once you see Listening written on the Screen.")
            print("Listening .....")
            sr.pause_threshold = 1
            audio = r.listen(source)
            #captured_audio = r.record(source, duration=50)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print('user said : ', query)
            #speak("Sir, You said.")
            #speak(query)
            a[0] = 1
        except Exception as e:
            speak("say that again please......")
            a[0] = 0
            #return query
if __name__ == "__main__":
    takecommand()
