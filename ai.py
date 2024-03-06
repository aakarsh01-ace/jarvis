import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) the voices[0].id is simply the voice behind jarvis

engine.setProperty('voices', voices[1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait( )  # wait until audio finishes playing
    
# voice to text
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

# Greetings
def greet():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Cypher. How may I assist you")

if  __name__ == "__main__":
    greet()
    while True:
    #if 1:
        query = takeCommand().lower()
        
        #logic for building tasks
        if "open notepad" in query:
            path = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(path)
            
        elif "open word" in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(path)   
            
        #elif "write a note" in query or 'note':
            #speak("What should I take a note of?")
            #note = takeCommand()
            #speak(f"You said, {note}. I will make a note of it.")
            #with open("notes.txt", "a") as f:
                #f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {note}\n")
            #speak("Note has been added to the file 'notes.txt'.")
                     
        elif "open fox" in query:
            path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(path)
        
        elif "open command" in query:
            os.system("start cmd")
            
        elif "camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "get ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}") 
        
        elif "wikipedia" in query:
            speak("searching wiki...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            speak(result)
            print(result)    
                
        # this will take you to youtube's home page   
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")
        
        # know the difference, this  one will only work for playing any random video you ask
        elif "play on youtube" in query:
            speak("Sir, which video should I play?") 
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")
            
            
        elif "search" in query:
            speak("What would you like to search for?")
            cm = takeCommand().lower()
            kit.search(f"{cm}")
            
        elif "sleep" in query:
            speak("Affimative, Sir")
            speak("Let me know if you have any other work.")
            sys.exit()
        speak("Sir, what's next on the list?")
        