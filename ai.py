import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) the voices[0].id is simply the voice behind jarvis

engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait( )  # wait until audio finishes playing
    

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout= 5, phrase_time_limit=10)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}")
        
    except Exception as e:
        speak("Sat that again please...")
        return "none"
    return query
    

if  __name__ == "__main__":
    takeCommand()
    #speak("Hello Sir, I am Jarvis")