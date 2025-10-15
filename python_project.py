import speech_recognition as sr
import pyttsx3
import wikipediaapi
import webbrowser
import datetime
import time
import os
import subprocess
import difflib

# Initialize speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()
wiki = wikipediaapi.Wikipedia(language='en', user_agent='assistant_v2')

def speak(text):
    """Speak the given text."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen for user voice input."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn’t catch that.")
        except sr.RequestError:
            speak("Speech service is unavailable right now.")
        return ""

def search_wikipedia(query):
    """Search and read Wikipedia summary."""
    page = wiki.page(query)
    if page.exists():
        summary = page.summary[:400]
        speak(summary)
    else:
        speak(f"I couldn’t find information about {query}.")

def open_website(site):
    """Open a website with or without common domain."""
    domains = [".com", ".org", ".net"]
    if not any(d in site for d in domains):
        site += ".com"
    if not site.startswith("https://"):
        site = "https://" + site
    webbrowser.open(site)
    speak(f"I opened {site}")

def system_command(cmd):
    """Perform system-level operations."""
    if cmd == "shutdown":
        speak("Shutting down your computer.")
        os.system("shutdown /s /t 1")
    elif cmd == "restart":
        speak("Restarting your computer.")
        os.system("shutdown /r /t 1")
    elif cmd == "lock":
        speak("Locking your computer.")
        if os.name == 'nt':
            os.system("rundll32.exe user32.dll,LockWorkStation")
        else:
            subprocess.call(['gnome-screensaver-command', '--lock'])
    else:
        speak("Unknown system command.")

def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is " + now)

notes_file = "voice_notes.txt"

def add_note(note):
    with open(notes_file, "a", encoding="utf-8") as f:
        f.write(note + "\n")
    speak("Note added.")

def list_notes():
    if not os.path.exists(notes_file):
        speak("No notes found.")
        return
    with open(notes_file, "r", encoding="utf-8") as f:
        notes = f.readlines()
    if not notes:
        speak("Your notes are empty.")
    else:
        for note in notes[-3:]:  # Read only last 3 notes for brevity
            speak(note.strip())

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet_msg = "Good morning!"
    elif hour < 18:
        greet_msg = "Good afternoon!"
    else:
        greet_msg = "Good evening!"
    speak(f"{greet_msg} How can I assist you today?")

COMMANDS = {
    "wikipedia": search_wikipedia,
    "open": open_website,
    "shutdown": lambda _: system_command("shutdown"),
    "restart": lambda _: system_command("restart"),
    "lock": lambda _: system_command("lock"),
    "time": lambda _: get_time(),
    "add note": add_note,
    "show notes": lambda _: list_notes(),
    "list notes": lambda _: list_notes(),
}

def process_command(cmd):
    """Process recognized commands."""
    for keyword, action in COMMANDS.items():
        if keyword in cmd:
            param = cmd.replace(keyword, "", 1).strip()
            action(param)
            return
    if any(word in cmd for word in ["hello", "hi", "how are you"]):
        greet()
    elif any(word in cmd for word in ["exit", "quit", "bye"]):
        speak("Goodbye!")
        exit(0)
    else:
        # Suggest closest known command
        suggestion = difflib.get_close_matches(cmd, COMMANDS.keys(), n=1)
        if suggestion:
            speak(f"Did you mean {suggestion[0]}?")
        else:
            speak("Sorry, I didn’t understand that command.")

if __name__ == '__main__':
    speak("Voice assistant initialized successfully.")
    greet()
    while True:
        command = listen()
        if command:
            process_command(command)
