import streamlit as st
from crewai_app.crew import build_crew
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="🌍",
    layout="centered"
)

# --- Header and Hero Section ---
st.markdown(
    """
    <div style='
        background: linear-gradient(90deg, #e0eafc 0%, #cfdef3 100%);
        padding: 32px 24px;
        border-radius: 16px;
        margin-bottom: 32px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    '>
        <h1 style='color:#222;font-size:2.5rem;margin-bottom:0.5em;'>🌍 AI-Powered Trip Planner</h1>
        <p style='font-size:1.2rem;color:#444;margin-bottom:0.5em;'>
            <b>Plan your next adventure in seconds.</b> <br>
            Enter your travel details, and our AI will craft a personalized itinerary for you!
        </p>
        <ul style='font-size:1.08rem; color:#444; margin-left:1.2em;'>
            <li>🎡 <b>Top attractions</b> tailored to your interests</li>
            <li>💰 <b>Accommodation & budget tips</b></li>
            <li>🍕 <b>Local food recommendations</b></li>
            <li>🚆 <b>Transport & visa details</b></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

# --- User Inputs ---
with st.form("trip_form"):
    st.markdown("#### 📝 Enter Your Trip Details")
    col1, col2 = st.columns(2)
    with col1:
        from_city = st.text_input("🏡 Departure City", "Bengaluru")
        date_from = st.date_input(
            "🗓️ Departure Date",
            value=datetime.date(2025, 5, 17)
        )
    with col2:
        destination_city = st.text_input("✈️ Destination City", "Paris")
        date_to = st.date_input(
            "🗓️ Return Date",
            value=datetime.date(2025, 5, 19)
        )
    interests = st.text_area(
        "🎯 Your Interests (e.g., museums, food, adventure, monuments)",
        "museums, food, adventure, monuments"
    )
    submitted = st.form_submit_button("🚀 Generate My AI Travel Plan")

# --- Generate & Display Travel Plan ---
if submitted:
    missing_fields = not all([from_city, destination_city, date_from, date_to, interests])
    if missing_fields:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    else:
        with st.spinner("⏳ AI is preparing your personalized travel itinerary..."):
            crew = build_crew(from_city, destination_city, interests, date_from, date_to)
            result = crew.kickoff()
        st.success("✅ Your AI-Powered Travel Plan is ready!")
        st.markdown("---")
        st.markdown(result)

        st.download_button(
            label="📥 Download Your Travel Plan",
            data=str(result),
            file_name=f"Travel_Plan_{destination_city}.txt",
            mime="text/plain"
        )
