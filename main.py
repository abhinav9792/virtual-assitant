from logging import exception
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
print(voice[0].id)
engine.setProperty("voice",voice[0].id)
engine.say("hello how are you")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hours = int(datetime.datetime.now().hour)
    if hours > 0 and hours <12 :
        speak("good morning")
    elif hours > 12 and hours < 18 :
        speak("good afternoon")
    else:
        speak("good evening")  

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recogniszing...")
        query = r.recognize_google(audio,language ="en-in")
        print(query)
    except exception as e:
        print("No voice found...")
        return "None"
    return query


# speak("Abhinav")
wishme()
takecommand()

