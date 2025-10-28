# To Print all the languages that google
# translator supports
# print(googletrans.LANGUAGES) # te for telugu, kn for kannada

# Importing necessary modules required
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# Function to convert text to speech
def recognize_speech(recog,source):
    print("Speak Anything :")
    audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio)
        print("You said : {}".format(text))
        return text
    except:
        print("Sorry could not recognize your voice")
        return None


def translate(text, src_lang,dest_lang):
    translator = Translator()
    translated = translator.translate(text, src_lang,dest=dest_lang)
    print(f"Translated from {src_lang} to {dest_lang}: {translated.text}")
    return translated.text 

recog1 = spr.Recognizer()
mc = spr.Microphone()

# Capture initial voice
with mc as source:
    print("Speak 'hello' to initiate the Translation!")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    MyText = recognize_speech(recog1, source)

# Check if the input contains 'hello'
if MyText and 'hello' in MyText:
    print("Initiating Translation...")
    #Source and target languages
    from_lang = 'te'
    to_lang = 'kn'
    
    with mc as source:
        print(f"Speak something in {from_lang}...")
        MyText = recognize_speech(recog1, source)
        
        if MyText:
            try:
                text_to_translate = translate(MyText, from_lang, to_lang)
                # Convert the translated text to speech
                output = gTTS(text=text_to_translate, lang=to_lang, slow=False)
                # store in a file
                output.save("translated_output.mp3")
                # Play the converted file
                os.system("start translated_output.mp3")  # For Windows, use "afplay" for MacOS or "xdg-open" for Linux
            except Exception as e:
                print(f"An Error Occurred: {e}")
        else:
            print("No speech recognized to translate.")
            exit()
    