import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time

# ---------- Voice ----------
engine = pyttsx3.init()
engine.setProperty("rate", 145)

def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

# ---------- Listen ----------
r = sr.Recognizer()

def listen(timeout=5):
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=timeout)
        except:
            return ""
    try:
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except:
        return ""

# ---------- Start ----------
speak("Jarvis online. Say hey jarvis.")

while True:
    wake = listen()

    if "hey jarvis" in wake:
        speak("Yes boss")

        time.sleep(0.5)

        command = listen()

        if command == "":
            speak("I did not hear that")
            continue

        if "hello" in command:
            speak("Hello boss")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "exit" in command or "stop" in command:
            speak("Shutting down. Goodbye boss.")
            break

        else:
            speak("Command not recognized")
