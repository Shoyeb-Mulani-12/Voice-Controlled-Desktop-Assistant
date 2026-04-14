import streamlit as st
import datetime
import psutil

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Desktop Assistant",
    page_icon="🤖",
    layout="centered"
)

# ------------------ HEADER ------------------
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🤖 AI Desktop Assistant</h1>
    <h4 style='text-align: center;'>Created by Shoyeb Hamid Mulani</h4>
    <hr>
""", unsafe_allow_html=True)

# ------------------ RESPONSE FUNCTION ------------------
def speak(text):
    st.success(text)

# ------------------ SIDEBAR ------------------
st.sidebar.title("📌 Navigation")
option = st.sidebar.radio("Choose Feature", [
    "🏠 Home",
    "⏰ Time & Date",
    "🌐 Quick Access",
    "💻 System Health"
])

# ------------------ HOME ------------------
if option == "🏠 Home":
    st.subheader("Welcome 👋")
    st.write("This is your Web-Based Desktop Assistant.")
    
    st.info("""
    ⚠ Limitations in Web Version:
    - No microphone access
    - No system control (shutdown, notepad, etc.)
    
    👉 Full features available in local version
    """)


# ------------------ TIME & DATE ------------------
import pytz

elif option == "⏰ Time & Date":
    st.subheader("⏰ Time & Date")

    ist = pytz.timezone('Asia/Kolkata')

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Show Time"):
            current_time = datetime.datetime.now(ist).strftime("%I:%M %p")
            speak(f"Current Time: {current_time}")

    with col2:
        if st.button("Show Date"):
            today_date = datetime.datetime.now(ist).strftime("%B %d, %Y")
            speak(f"Today's Date: {today_date}")

# ------------------ QUICK ACCESS ------------------
elif option == "🌐 Quick Access":
    st.subheader("🌐 Open Websites")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔗 Popular")
        st.markdown("[▶ Google](https://www.google.com)")
        st.markdown("[▶ YouTube](https://www.youtube.com)")

    with col2:
        st.markdown("### 💼 Professional")
        st.markdown("[▶ GitHub](https://github.com)")
        st.markdown("[▶ LinkedIn](https://linkedin.com)")

# ------------------ SYSTEM HEALTH ------------------
elif option == "💻 System Health":
    st.subheader("💻 System Health")

    if st.button("Check System Health"):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        st.write(f"🧠 CPU Usage: {cpu}%")
        st.write(f"📊 RAM Usage: {ram}%")

        speak(f"CPU is {cpu}% and RAM is {ram}%")

# ------------------ FOOTER ------------------
st.markdown("""
    <hr>
    <p style='text-align: center; color: grey;'>
    🚀 MCA Final Year Project | Built with Streamlit
    </p>
""", unsafe_allow_html=True)
