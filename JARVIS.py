import datetime
from time import time
import pyttsx3
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Sire!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sire!")
    
    else:
        speak("Good Evening Sire!")  
        
    speak("I am Jarvis Sire! Please tell me what can i do for you.")  

def takeCommand():
    #It take mic input and returns string output
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
         
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query

def open_calculator():
  
    os.system("calc")

def perform_calculation(query):
  
    try:
        query = query.lower()
        
        
        query = query.replace('plus', '+')
        query = query.replace('minus', '-')
        query = query.replace('multiply', '*')
        query = query.replace('times', '*')
        query = query.replace('divide', '/')
        query = query.replace('by', '/')
        
        datetime.time.sleep(1)
        
        for char in query:
            pyautogui.write(char)
            time.sleep(0.1)
            
        pyautogui.press('enter')        
        
        
        result = eval(query)  
        speak(f"The result is {result}")
        print(f"Result: {result}")
        
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I couldn't understand the calculation.")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emialgiven', 'password-given')
    server.sendemail('emailgiven', to, content)
    server.close()
     
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if 'open calculator' in query:
            speak("Opening calculator, Sire!")
            open_calculator()

        # Perform calculations
        elif 'calculate' in query:
            speak("What should I calculate, Sire?")
            calc_query = takeCommand().lower()
            perform_calculation(calc_query)
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open online music' in query:
            speak("Opening your o Music playlist, Sire!")
            playlist_url = "https://music.youtube.com/playlist?list=PLKPOMFL6VZaHV2VzJVDjb6y2I7eGYSqId"
            webbrowser.open(playlist_url) 
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Devang Chaudhary\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to Devang' in query:
            try: 
                speak("What should I say?")
                content = takeCommand()
                to = "Devanshch9911@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)       
                speak("Sorry my sire devang. I am not able to send this email to sender")
        elif 'exit' in query:
            speak("Goodbye, Sire!")
            break