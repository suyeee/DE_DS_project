from datetime import datetime
from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    'start_date': datetime(2022, 7, 24)
}

with DAG(
    dag_id="forest_fire_forecast_model_pipeline",
    schedule_interval="@monthly",
    default_args=default_args,
    tags=["forest", "fire", "forecast","model","homemade", "pipeline"],
    catchup=False) as dag:

    montly_preprocess = BashOperator(
        bash_command="python /home/lab20/airflow/dags/montly_preprocess.py",
        task_id='montly_preprocess'
    )
    montly_model_training = BashOperator(
        bash_command='python /home/lab20/airflow/dags/montly_model_training.py',
        task_id="montly_model_training"
    )

    montly_preprocess >> montly_model_training