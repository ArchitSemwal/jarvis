import pyttsx3 
import datetime


engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)    
    month = int(datetime.datetime.now().month)    
    date = int(datetime.datetime.now().day)    
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    speak("Welcome back sir!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir")

    speak(" Sir this is jarvis your personal assistant all your gaming accessories will be ready in few minutes so the time sir you can grab a cup of coffee and enjoy your day")

wishme()