# 🎬 Feature Flag-Based Recommendation Rollout (Flask + Unleash)

This project demonstrates a 20% gradual rollout of a new movie recommendation model using [Unleash](https://www.getunleash.io/) feature flags in a Flask application.

---

## 📁 Project Files

- `app.py`: Flask API serving `/recommend` endpoint
- `simulate_requests.py`: Simulates 100 users and counts rollout split
- `requirements.txt`: Project dependencies

---

## ⚙️ Setup Instructions

### 1. Clone this repository

```bash
git clone git@github.com:YashwanthYS/Unleash_Flask_App.git
cd unleash-flask-recommendation
```

### 2. Set up requirements

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3. Set up Unleash

git clone https://github.com/Unleash/unleash.git
cd unleash
docker compose up -d


### 4. Create flag

Access the Unleash dashboard and create the flag

### 5. Run the Application

python app.py
python simulate_requests.py

