# Daily Weather Data Pipeline with Apache Airflow

This project demonstrates a basic ETL data pipeline using Apache Airflow. It fetches daily weather data from OpenWeatherMap API, transforms it, and stores it into a SQLite database.

## 📦 Project Structure
```
weather_pipeline/
├── dags/
│   └── daily_weather_dag.py
├── weather_utils/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── requirements.txt
└── README.md
```

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/weather_pipeline.git
cd weather_pipeline
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### 3. Set up Airflow
Use the official Docker setup for simplicity:
```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'
docker-compose up airflow-init
docker-compose up
```

Access Airflow UI at: [http://localhost:8080](http://localhost:8080)

### 4. Add Your Weather API Key
In `extract.py`, replace `your_api_key` with your actual OpenWeatherMap API key.

### 5. Run the DAG
Trigger the `daily_weather_dag` from the Airflow UI or wait for it to run on schedule.

## ✅ Output
A SQLite database (`weather.db`) in `/tmp` with daily weather records.

## 🧠 Future Improvements
- Add Slack/Email alerts for extreme weather
- Store data in cloud DB (Postgres, BigQuery)
- Visualize with Streamlit or Dash

---

Happy Orchestrating! 🌤
