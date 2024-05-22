import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

#Taking Voice From the System
engine =pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

 

engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

#Create a speak function 
def speakfunc(text):

    engine.say(text)
    engine.runAndWait()


#speech recognization function 
def takecommandfunc():
    """
    this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening my voice..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query 


#The function for wish me by using time
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speakfunc("Good morning sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speakfunc("Good afternoon sir. How are you doing")

    else:
        speakfunc("Good evening sir. How are you doing")
    
    speakfunc("I am JARVIS. Tell me sir how can i help you")



# text=takecommandfunc()
# speakfunc(text)


if __name__=="__main__":
   wish_me()
   while True:
        
    query=takecommandfunc().lower()
    
    if "wikipedia" in query:
            speakfunc("Searching Wikipedia")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speakfunc("According to Wikipedia")
            print(results)
            speakfunc(results)


    elif "youtube" in query:
        speakfunc("Opening YouTube")
        webbrowser.open("youtube.com")

    elif "github" in query:
                speakfunc("Opening github")
                webbrowser.open("github.com")

    elif "google" in query:
                speakfunc("Opening google")
                webbrowser.open("google.com")

    
    elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speakfunc(f"Sir the time is {strTime}")
    
    elif 'goodbye' in query:
                speakfunc("ok sir. I am always here for you. bye bye")
                exit()

       

    
    

       
  









 
 
