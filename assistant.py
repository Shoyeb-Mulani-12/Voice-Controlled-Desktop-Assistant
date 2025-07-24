import sys
import speech_recognition as sr
import pyttsx3
import psutil
import pyautogui
import webbrowser
import os
import datetime
import subprocess
import ctypes
import random

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command(first_time=False):
    if first_time:
        print("\n:- Voice Controlled Desktop Assistant by Shoyeb Hamid Mulani -:")
        print("\n-> Try saying:")
        print("- Open Notepad")
        print("- Open Calculator")
        print("- Check battery")
        print("- What is the time")
        print("- What is today's date")
        print("- Play music")
        print("- Search")
        print("- Open YouTube")
        print("- Open file explorer")
        print("- Open browser")
        print("- Check system health")
        print("- Lock system")
        print("- Shutdown")
        print("- Restart")
        print("- Sleep")
        print("- Exit")
        print("\n  Note: Internet connection is required for voice recognition and search.\n")

    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        if first_time:
            speak("Hi, I am your Desktop Assistant, created by Shoyeb Hamid Mulani.")
            speak("You can say commands like: open notepad, check battery, play music, or open YouTube.")
            speak("Now, how can I help you?")
        else:
            speak("How can I help you?")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-IN')
        print(f"User said: {query}")
    except Exception:
        print("Sorry, I didn't catch that, please try again")
        speak("Sorry, I didn't catch that, please try again")
        return None
    return query.lower()

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Your battery is at {percent} percent.")

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The current time is {current_time}.")

def get_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def open_notepad():
    speak("Opening Notepad.")
    os.system("notepad")

def open_calculator():
    speak("Opening Calculator.")
    subprocess.Popen('calc.exe')

def search_google():
    speak("What should I search on Google?")
    query = take_command()
    if query:
        speak(f"Searching {query} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={query}")

def lock_system():
    speak("Locking the device.")
    ctypes.windll.user32.LockWorkStation()

def shutdown():
    speak("Shutting down the computer.")
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the computer.")
    os.system("shutdown /r /t 1")

def sleep():
    speak("Putting the computer to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def play_music():
    music_dir = os.path.join(os.path.expanduser("~"), "Music")
    if not os.path.exists(music_dir):
        speak("Sorry, I couldn't find your Music folder.")
        return
    songs = [file for file in os.listdir(music_dir) if file.lower().endswith(('.mp3', '.wav'))]
    if songs:
        song = random.choice(songs)
        song_path = os.path.join(music_dir, song)
        speak(f"Playing {song}")
        os.startfile(song_path)
    else:
        speak("No songs found in your Music folder.")

def open_youtube():
    speak("Opening YouTube.")
    webbrowser.open("https://www.youtube.com")

def open_file_explorer():
    speak("Opening File Explorer.")
    path = os.path.expanduser("~")
    os.startfile(path)

def open_browser():
    speak("Opening your default browser.")
    webbrowser.open("https://www.google.com")

def system_health():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    speak(f"CPU is at {cpu} percent and RAM usage is {ram} percent.")

def main():
    first_time = True
    while True:
        query = take_command(first_time)
        first_time = False

        if query is None:
            continue

        handled = False

        if "battery" in query:
            check_battery()
            handled = True
        elif "time" in query:
            get_time()
            handled = True
        elif "date" in query:
            get_date()
            handled = True
        elif "notepad" in query:
            open_notepad()
            handled = True
        elif "calculator" in query:
            open_calculator()
            handled = True
        elif "search" in query:
            search_google()
            handled = True
        elif "lock" in query:
            lock_system()
            handled = True
        elif "shutdown" in query:
            shutdown()
            handled = True
        elif "restart" in query:
            restart()
            handled = True
        elif "sleep" in query:
            sleep()
            handled = True
        elif "play music" in query or "play song" in query:
            play_music()
            handled = True
        elif "open youtube" in query:
            open_youtube()
            handled = True
        elif "file explorer" in query or "open explorer" in query:
            open_file_explorer()
            handled = True
        elif "browser" in query:
            open_browser()
            handled = True
        elif "system" in query and "health" in query:
            system_health()
            handled = True
        elif "exit" in query or "quit" in query:
            speak("Goodbye! See you again!")
            break
        else:
            speak("Sorry, I didn't understand that command.")
            print("Unrecognized command. Please try again.")

        if handled:
            print("Task completed. Press Enter to continue...")
            speak("Task completed. Press Enter to continue...")
            input()


if __name__ == "__main__":
    main()
