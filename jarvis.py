import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# FIX 1: Initialize engine OUTSIDE the function
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait() 

def listen(timeout=5):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            # FIX 2: Adjust for background noise (fan, AC, etc.)
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            audio = r.listen(source, timeout=timeout, phrase_time_limit=5)
            text = r.recognize_google(audio)
            print("You:", text)
            return text.lower()
    except:
        return ""

# Main System
speak("Hi boss. I am Jarvis. Say hey jarvis to activate the system.")

while True:
    wake = listen(timeout=4)

    if "hey jarvis" in wake:
        speak("Access Granted. Welcome boss")

        command = listen(timeout=6)

        if "hello" in command:
            speak("Hello my boss")

        elif "time" in command:
            speak("Now " + datetime.datetime.now().strftime("%I:%M %p"))

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "exit" in command or "stop" in command:
            speak("Enjoy boss")
            break
        
        # FIX 3: prevent "Access denied" when you just stay silent
        elif command == "":
            speak("I didn't hear anything")

        else:
            speak("Access denied")