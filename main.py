import speech_recognition as sr
import webbrowser as wb
import pyttsx3 as pt
import os
import subprocess as sp

# Initialize TTS engine
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)
        return query.lower()

    except:
        speak("Sorry, I didn't catch that")
        return ""

if __name__ == "__main__":
    speak("Alexa is online. How may I help you?")

    while True:
        command = listen()

        if "open youtube" in command:
            speak("Opening YouTube")
            wb.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            wb.open("https://google.com")

        elif "exit" in command:
            speak("Shutting down")
            break