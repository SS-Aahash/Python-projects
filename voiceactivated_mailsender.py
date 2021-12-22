import os
import smtplib
from email.message import EmailMessage
import speech_recognition as sr
from text_to_speech import *

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("Sir, You can start to talk once you see Listening written on the Screen.")
        print("Listening .....")
        #sr.pause_threshold = 1
        audio = r.listen(source)
        #captured_audio = r.record(source, duration=50)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        
        #speak("Sir, You said.")
       #speak(query)
    except Exception as e:
        speak("say that again please......")
    return query

myemail = os.environ.get("email_id")
password = os.environ.get("email_pass")
msg  = EmailMessage()
print("Sir, what would be the subject of your mail.")
speak("sir, what would be the subject of your mail.")
msg["Subject"] = takecommand()
msg['From'] = myemail
#msg['To'] = "sankari4321@gmail.com"
msg['To'] = "moccer@protonmail.com"
print("Tell me the message")
speak("Tell me the message")
subject = takecommand()
msg.set_content(subject)
#message = f"Subject: printouts!!!\nactivated"


with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
    #server.starttls() #to encript the traffic
    server.login(myemail,password)
    print("           Email preview\n====================================")
    print(f"To : {msg['To']}")
    print(f"Subject : {msg['Subject']}")
    print(f"Message : {subject}")
    speak("Please, preview your email and Confirm to send the mail.")
    confirmation = takecommand()
    if "yes" in confirmation:
        server.send_message(msg)
        speak("your message has been sent sir")
    else:
        pass



    



