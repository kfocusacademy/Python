# Building a virtual assistant to answer the below queries
# 1. Query from wikipedia
# 2. Open a website

import webbrowser
import wikipedia
import pyttsx3
import speech_recognition as sr
import requests
import datetime
import time
import sys

# Function to convert text to speech
def speak(command):
    
    #initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices
    engine.say(command)
    engine.runAndWait()

# Function to greet the user
def hello():
    speak("Hello, I am your virtual assistant. How can I help you?")
    
# this method will take the query from the user and return it as a string
def takeQuery():
    hello()
    
    while(True):
        
        # Converting the command in lower case
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")  
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'your name' in query:
            speak("My name is Friday, your desktop assitant")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")
        elif 'exit' in query:
            speak("Thanks for using me. Have a nice day")
            sys.exit()
        elif 'bye' in query:
            speak("Thanks for using me. Have a nice day")
            sys.exit()
        else:
            speak("I can search it on google for you")
            webbrowser.open("www.google.com/search?q="+query)


# this method will take the command from the user and return it as a string
def takeCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
        return query

# Main function
if __name__ == "__main__": 
    takeQuery()


