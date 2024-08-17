import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser


#Taking voice from my system

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
# print(type(voices))

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)
#speak function

def speak(text):
    """This function takes the text and returns the voice
    
    Args:
        text(__type__):string
    """
    engine.say(text)
    engine.runAndWait()

# speak("hello i am a python priogrammer. How are you")

#Speech recoginition funtion

def takeCommand():
    """This function will recognize voice and returns text


    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("recognizing .....")
            query=r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            print("say that again please")
            return "None"
        
        return query
    

text=takeCommand()
speak(text)