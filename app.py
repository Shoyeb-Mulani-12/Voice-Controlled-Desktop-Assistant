import streamlit as st
import datetime
import psutil

# Page config
st.set_page_config(page_title="AI Desktop Assistant", page_icon="🤖", layout="centered")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🤖 AI Desktop Assistant</h1>
    <h4 style='text-align: center;'>Created by Shoyeb Hamid Mulani</h4>
    <hr>
""", unsafe_allow_html=True)

# Function to display response
def speak(text):
    st.success(text)

# Sidebar
st.sidebar.title("📌 Menu")
option = st.sidebar.radio("Choose Action", [
    "🏠 Home",
    "🔋 Battery Status",
    "⏰ Time & Date",
    "🌐 Open Websites",
    "💻 System Health"
])

# HOME
if option == "🏠 Home":
    st.subheader("Welcome 👋")
    st.write("This is your Web-Based Desktop Assistant.")
    st.info("Note: Voice and system controls work only in local version.")

# BATTERY
elif option == "🔋 Battery Status":
    st.subheader("🔋 Battery Status")
   if st.button("Check Battery"):
    battery = psutil.sensors_battery()

    if battery:
        percent = battery.percent
        st.progress(percent)
        speak(f"Battery is at {percent}%")
    else:
        st.warning("⚠ Battery data not available on server")

# TIME & DATE
elif option == "⏰ Time & Date":
    st.subheader("⏰ Time & Date")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Time"):
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Current Time: {time}")

    with col2:
        if st.button("Show Date"):
            date = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's Date: {date}")

# WEBSITES
elif option == "🌐 Open Websites":
    st.subheader("🌐 Quick Access")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("[▶ Open Google](https://www.google.com)")
        st.markdown("[▶ Open YouTube](https://www.youtube.com)")

    with col2:
        st.markdown("[▶ Open GitHub](https://github.com)")
        st.markdown("[▶ Open LinkedIn](https://linkedin.com)")

# SYSTEM HEALTH
elif option == "💻 System Health":
    st.subheader("💻 System Health")

    if st.button("Check System Health"):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        speak(f"CPU Usage: {cpu}% | RAM Usage: {ram}%")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>
    🚀 Built with Streamlit | MCA Final Year Project
    </p>
""", unsafe_allow_html=True)
