import streamlit as st
import datetime
import psutil
import webbrowser

st.set_page_config(page_title="Desktop Assistant", layout="centered")

st.title(" Voice Controlled Desktop Assistant (Web Version)")
st.write("Created by Shoyeb Hamid Mulani")

command = st.text_input("Enter your command:")

def speak(text):
    st.success(f"Assistant: {text}")

if command:
    query = command.lower()

    if "battery" in query:
        battery = psutil.sensors_battery()
        percent = battery.percent if battery else "Not available"
        speak(f"Battery is at {percent}%")

    elif "time" in query:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {now}")

    elif "date" in query:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "open youtube" in query:
        speak("Opening YouTube")
        st.markdown("[Open YouTube](https://www.youtube.com)")

    elif "open google" in query:
        speak("Opening Google")
        st.markdown("[Open Google](https://www.google.com)")

    elif "search" in query:
        search_query = st.text_input("What do you want to search?")
        if search_query:
            st.markdown(f"[Search {search_query}](https://www.google.com/search?q={search_query})")

    elif "system health" in query:
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        speak(f"CPU: {cpu}% | RAM: {ram}%")

    elif "notepad" in query or "calculator" in query:
        speak("This feature works only in local system (not supported on web)")

    elif "shutdown" in query or "restart" in query:
        speak("System control commands are disabled in web version")

    elif "exit" in query:
        speak("Goodbye!")

    else:
        speak("Sorry, I didn't understand that command")