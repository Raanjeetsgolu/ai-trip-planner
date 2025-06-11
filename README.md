# 🌍 AI Trip Planner

**AI Trip Planner** is a smart, agentic travel assistant built with **Streamlit**, **CrewAI**, and **OpenAI**. It generates personalized travel itineraries based on your interests, travel dates, and destination—leveraging LLMs and real-time web search tools.

---

## ✨ Features

- **Personalized Itineraries** – Attractions, food, and experiences tailored to your interests.  
- **Travel Logistics** – Practical tips on transport, visas, and local customs.  
- **Agentic AI** – CrewAI agents for local expertise, logistics, and planning.  
- **Modern UI** – Simple, beautiful Streamlit interface.  
- **Downloadable Plans** – Export your itinerary as a text file.  

---

## 🚀 Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/Raanjeetsgolu/ai-trip-planner.git
cd ai-trip-planner
```

### 2. Set Up Your Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your-openai-api-key
```

> ⚠️ **Do not commit your `.env` file.** It is already included in `.gitignore`.

---

### 4. Run the App

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## 🐳 Run Using Docker

Run the container:

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your-openai-api-key raanjeetsgolu/ai-trip-planner:latest
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Feel free to submit issues or pull requests! Let's make travel planning smarter together. 🌐✈️
