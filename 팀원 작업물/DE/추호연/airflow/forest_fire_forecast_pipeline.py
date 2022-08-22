from datetime import datetime
from airflow import DAG
# from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
# from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


default_args = {
    'start_date': datetime(2022, 1, 1)
}

with DAG(
    dag_id="forest_fire_forecast_pipeline",
    schedule_interval="@hourly",
    default_args=default_args,
    tags=["forest", "fire", "forecast", "pipeline"],
    catchup=False) as dag:

    forest_fire_forecast_get_data = BashOperator(
        bash_command="python /home/lab20/airflow/dags/forest_fire_forecast_get_data.py",
        task_id='forest_fire_forecast_get_data'
    )

    # forest_fire_forcast_preprocess = SparkSubmitOperator(
    #     application='/home/lab20/airflow/dags/forest_fire_forcast_preprocess.py',
    #     task_id="preprocess",
    #     conn_id="spark_local"
    # )

    # movie_rec = SparkSubmitOperator(
    #     application='/home/tutor/airflow/dags/movie-rec.py',
    #     task_id='movie-rec',
    #     conn_id='spark_local'
    # )

    # get_data >> preprocess
    forest_fire_forecast_get_data