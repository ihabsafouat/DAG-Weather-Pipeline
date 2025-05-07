from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from weather_utils import extract, transform, load

default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

with DAG('daily_weather_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_task = PythonOperator(
        task_id='extract_weather',
        python_callable=extract.get_weather_data,
    )

    transform_task = PythonOperator(
        task_id='transform_weather',
        python_callable=transform.clean_weather_data,
    )

    load_task = PythonOperator(
        task_id='load_weather',
        python_callable=load.save_weather_data,
    )

    extract_task >> transform_task >> load_task
