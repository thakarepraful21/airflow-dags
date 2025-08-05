from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'test_dag',
    default_args=default_args,
    description='Simple test DAG',
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
) as dag:

    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    sleep_task = BashOperator(
        task_id='sleep_task',
        bash_command='sleep 5',
    )

    print_date >> sleep_task
