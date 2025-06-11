FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8501

# (Optional) Document the env variable
ENV OPENAI_API_KEY=""

CMD ["streamlit", "run", "app.py"]
