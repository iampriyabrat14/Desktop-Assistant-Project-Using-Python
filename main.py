import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

#Taking Voice From the System
engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)
# print(type(voices))

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

#Create a speak function 
def speakfunc(text):

    engine.say(text)
    engine.runAndWait()


#
def takecommandfunc():
    """
    this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening my voice..........")
   






 
 
