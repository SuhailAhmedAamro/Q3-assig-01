import streamlit as st
import random
import time
import pandas as pd
import matplotlib.pyplot as plt

# ==== MOTIVATIONAL QUOTES ====
quotes = [
    "Your potential is endless!",
    "Every day is a chance to improve!",
    "Believe in yourself and grow!",
    "Hard work beats talent when talent doesn’t work hard!",
    "Failure is not the opposite of success; it’s part of success!"
]

# ==== USER AUTHENTICATION ====
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# ==== ADDING CSS FOR ANIMATIONS & HOVER EFFECTS ====
st.markdown("""
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .fade-in {
            animation: fadeIn 2s;
        }
        .stButton>button:hover {
            background-color: #28a745 !important;
            color: white !important;
            transform: scale(1.05);
            transition: all 0.3s ease-in-out;
        }
        .sidebar-hidden { display: none !important; }
        .navbar-user {
            position: absolute;
            top: 10px;
            right: 20px;
            font-size: 18px;
            font-weight: bold;
            background-color: #007BFF;
            color: white;
            padding: 10px;
            border-radius: 50px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🚀💡")
st.sidebar.subheader("🔑 User Login")

user_name = st.sidebar.text_input("Enter Your Name")
user_password = st.sidebar.text_input("Enter Password", type="password")

if st.sidebar.button("Login"):
    if user_name and user_password:
        st.sidebar.success(f"Welcome, {user_name}!")
        st.session_state["logged_in"] = True
    else:
        st.sidebar.error("Please enter valid credentials!")

if "logged_in" in st.session_state and st.session_state["logged_in"]:
    st.markdown(f'<div class="navbar-user">👤 {user_name}</div>', unsafe_allow_html=True)
    st.markdown("<style>.st-emotion-cache-1y4p8pa {display: none;}</style>", unsafe_allow_html=True)

# ==== MOTIVATIONAL QUOTE GENERATOR ====
st.subheader("💬 Get Your Motivation!")
if st.button("✨ Click for Motivation!", key="motivation_button"):
    with st.spinner("Fetching your daily boost..."):
        time.sleep(1)
        st.success(random.choice(quotes))

# ==== DAILY GOAL TRACKER ====
st.subheader("📌 Set Your Growth Goal")
daily_goal = st.text_input("What will you improve today?")
progress = st.slider("Progress Percentage", 0, 100, 50)

# Simulated Database for Completed Challenges
if "challenges" not in st.session_state:
    st.session_state["challenges"] = []

if st.button("💪 Submit Goal"):
    if daily_goal:
        st.success(f"✅ Great! Your goal **'{daily_goal}'** is saved with {progress}% progress! 🎯")
        st.session_state["challenges"].append({"Name": user_name, "Challenge": daily_goal, "Progress": progress})
    else:
        st.warning("Enter a goal before submitting!")

# ==== LEADERBOARD & COMPLETED CHALLENGES ====
st.subheader("🏆 Growth Leaderboard")

# Displaying Real-Time Completed Challenges
if len(st.session_state["challenges"]) > 0:
    st.write("### ✅ Completed Challenges")
    challenge_df = pd.DataFrame(st.session_state["challenges"])
    st.table(challenge_df.sort_values(by="Progress", ascending=False))

# ==== PROGRESS GRAPH ====
st.subheader("📊 Your Progress Chart")
fig, ax = plt.subplots()
if len(st.session_state["challenges"]) > 0:
    ax.bar(challenge_df["Name"], challenge_df["Progress"], color="skyblue")
    st.pyplot(fig)

# ==== FOOTER ====
st.markdown("""
---
💡 **Made with ❤️ by Suhail Ahmed Aamro**  
📌 **Follow for more projects** | 🌍 **[GitHub](https://github.com/SuhailAhmedAamro/Q3-assig-01/blob/main/growth_mindset_app/app.py)** | 📝 **[LinkedIn](https://www.linkedin.com/in/suhail-ahmed-aamro-623863279/)**
""", unsafe_allow_html=True)
