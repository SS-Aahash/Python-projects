from speechrecognition import takecommand
from text_to_speech import speak 
import subprocess

'''while True:
    query = takecommand().lower()
    
    #QUITING
    if "quit" or "go to sleep" in query:
        speak("as you wish sir, I'm gonna take a nap, see you.")
        break
    
    #INTRODUCTION
    if "name" in query:
        speak("My name is monday, I'am your personal assistant")'''

subprocess.Popen("notepad.exe")