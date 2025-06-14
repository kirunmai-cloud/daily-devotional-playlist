import streamlit as st
from datetime import datetime

# Updated daily playlist mapping with verified working links
playlists = {
    "Monday": {
        "deity": "Lord Shiva",
        "songs": [
            ("Shiva Tandava Stotram (Trance Version)", "https://www.youtube.com/watch?v=hMBKmQEPNzI"),
            ("Ye Bholya Shankara (Marathi Shiv Bhajan)", "https://www.youtube.com/watch?v=udeTZ4PfOQ8"),
        ],
    },
    "Tuesday": {
        "deity": "Lord Hanuman",
        "songs": [
            ("Shri Hanuman Chalisa (Bhakti Official)", "https://www.youtube.com/watch?v=QYsGoWwubmw"),
            ("Marathi Hanuman Bhajans — Anjanichya Soota", "https://www.youtube.com/watch?v=LwMu4PH-t-g"),
        ],
    },
    "Wednesday": {
        "deity": "Lord Krishna",
        "songs": [
            ("Krishna Bhajan & Mantra", "https://www.youtube.com/watch?v=ZJHoZt_zgmc"),
            ("Krishna Aarti Marathi", "https://www.youtube.com/watch?v=1DhIHOiuIxM"),
        ],
    },
    "Thursday": {
        "deity": "Sai Baba / Vishnu",
        "songs": [
            ("Sai Baba Bhajan (Marathi)", "https://www.youtube.com/watch?v=Ue7XT5zYGMA"),
            ("Vishnu Sahasranama", "https://www.youtube.com/watch?v=EwW61CDk4_k"),
        ],
    },
    "Friday": {
        "deity": "Goddess Lakshmi / Durga",
        "songs": [
            ("Lakshmi Aarti — Hindi", "https://youtu.be/SyqgAt-T0iQ?si=MIMkE-rKPDpqDNyA"),
            ("Durga Bhajan — Marathi", "https://www.youtube.com/watch?v=S3jE-IDaOKk"),
        ],
    },
    "Saturday": {
        "deity": "Shani Dev / Fun",
        "songs": [
            ("Hindi Chill Lo‑Fi Mix", "https://www.youtube.com/watch?v=8F3Q2iO6BMo"),
            ("Marathi Comedy Song", "https://www.youtube.com/watch?v=R5bq3VZNeUM"),
        ],
    },
    "Sunday": {
        "deity": "Surya Dev / Fun",
        "songs": [
            ("Hindi Morning Raga Mix", "https://youtu.be/3cm8znDThOE?si=i59o_2DKoGAXJewN"),
            ("Feel‑Good Marathi", "https://youtu.be/9QdEvmYwaKk?si=5KlezPWloVxX_2H0"),
        ],
    },
}

# Get current weekday
today = datetime.now().strftime("%A")
today_data = playlists.get(today, {"deity": "Unknown", "songs": []})

# Streamlit UI
st.set_page_config(page_title="Daily Devotional Playlist", page_icon="🎵")
st.title("🎧 Daily Devotional Playlist")
st.subheader(f"🗓️ Today is {today}")
st.markdown(f"🙏 Dedicated to **{today_data['deity']}**")

st.write("Here are your handpicked devotional and relaxing songs:")

for name, url in today_data["songs"]:
    st.markdown(f"▶️ [{name}]({url})", unsafe_allow_html=True)
