# Program to convert speech to text using SpeechRecognition library
import speech_recognition as sr
import os   
import pyttsx3

# initialize the recognizer
r  = sr.Recognizer()

# Function to convert text to speech

def speaktoText(command):
    
    #initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Change index for different voices
    engine.say(command)
    engine.runAndWait()
    
# Continue loop until user speaks 

while(1):
    
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            
            #listens for the user's input
            audio2 = r.listen(source2)
            
            # Using google to reognize audio
            myText = r.recognize_google(audio2)
            myText = myText.lower()
            
            # Print what user said 
            print("Did you say:",myText)
            speaktoText(myText)
    except sr.RequestError as e:
        print("Could not request results; {0}",format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
        
            
        

