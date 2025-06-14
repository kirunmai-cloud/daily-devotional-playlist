import streamlit as st
from datetime import datetime

# Daily playlist mapping
playlists = {
    "Monday": {
        "deity": "Lord Shiva",
        "songs": [
            ("Shiva Tandava Stotram", "https://www.youtube.com/watch?v=1HqF8YzWA0g"),
            ("Shiv Bhaktigeet (Marathi)", "https://www.youtube.com/watch?v=KHF-m5Q5mXw"),
        ],
    },
    "Tuesday": {
        "deity": "Lord Hanuman",
        "songs": [
            ("Hanuman Chalisa", "https://www.youtube.com/watch?v=AETFvQonfV8"),
            ("Marathi Hanuman Bhajan", "https://www.youtube.com/watch?v=1ySsYvU7ZrQ"),
        ],
    },
    "Wednesday": {
        "deity": "Lord Krishna",
        "songs": [
            ("Krishna Bhajan", "https://www.youtube.com/watch?v=zZz1dyZxTFY"),
            ("Krishna Aarti (Marathi)", "https://www.youtube.com/watch?v=u2T7wQ9gD5Q"),
        ],
    },
    "Thursday": {
        "deity": "Sai Baba / Vishnu",
        "songs": [
            ("Vishnu Sahasranama", "https://www.youtube.com/watch?v=1RwW7b-L520"),
            ("Sai Baba Bhajan (Marathi)", "https://www.youtube.com/watch?v=ThG5Obvrlj8"),
        ],
    },
    "Friday": {
        "deity": "Goddess Lakshmi / Durga",
        "songs": [
            ("Laxmi Aarti (Hindi)", "https://www.youtube.com/watch?v=I88Qj9g5NyA"),
            ("Durga Bhakti (Marathi)", "https://www.youtube.com/watch?v=XeFoFSdZCAc"),
        ],
    },
    "Saturday": {
        "deity": "Shani Dev / Fun",
        "songs": [
            ("Lo-Fi Chill Hindi", "https://www.youtube.com/watch?v=3nQNiWdeH2Q"),
            ("Marathi Comedy Song", "https://www.youtube.com/watch?v=IKPlfL7tTfE"),
        ],
    },
    "Sunday": {
        "deity": "Surya Dev / Fun",
        "songs": [
            ("Morning Vibes (Hindi)", "https://www.youtube.com/watch?v=Yb2kP9_dZ3A"),
            ("Feel-Good Marathi", "https://www.youtube.com/watch?v=Y9os_Bu48Wc"),
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
