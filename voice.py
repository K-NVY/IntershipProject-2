import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return None
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
from datetime import datetime


def tell_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is {current_time}"
import webbrowser

def open_website(url):
    webbrowser.open(url)
import os

def open_application(app_path):
    os.startfile(app_path)
import wikipedia
import webbrowser

def open_website(command):
    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
    elif "github" in command:
        webbrowser.open("https://www.github.com")
    else:
        # You can extract the site name dynamically
        site = command.replace("open ", "").strip()
        url = f"https://{site}.com"
        webbrowser.open(url)
    
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There's more than one result, please be more specific. Possible options: {e.options}"
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Wikipedia is not responding. Try again later."
def main():
    while True:
        command = listen()
        if command:
            command = command.lower()
            
            if 'time' in command:
                speak(tell_time())
            elif 'open' in command and 'website' in command:
                url = command.split(' ')[-1]  # Simplified
                speak(f"Opening {url}")
                open_website(url)
            elif "open" in command:
                open_website(command)

            elif 'launch' in command:
                app_name = command.split(' ')[-1]  # Simplified
                speak(f"Launching {app_name}")
                open_application(app_name)
            elif 'wikipedia' in command:
                search_query = command.replace("search", "").replace("wikipedia", "").strip()
                result = search_wikipedia(search_query)
                speak(result)
            elif 'exit' in command or 'quit' in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
