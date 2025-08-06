from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    dag_id='test_dag',
    default_args=default_args,
    description='Simple test DAG',
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
)

# Define the first task
print_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

# Define the second task
sleep_task = BashOperator(
    task_id='sleep_task',
    bash_command='sleep 5',
    dag=dag,
)

# Set task dependencies
print_date >> sleep_task