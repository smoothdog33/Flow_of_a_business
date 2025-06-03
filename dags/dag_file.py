from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import time

def print_start_message():
    print("Start task is executing...")
    time.sleep(5)  # Simulating the task running for a few seconds

def print_success_message():
    print("Ayan is a goofy guy")
    time.sleep(5)

def print_end_message():
    print("End task executed successfully!")
    time.sleep(5)

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 23),
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

# Instantiate the DAG
dag = DAG(
    'my_example_dag',
    default_args=default_args,
    description='An example DAG with frequent execution',
    schedule_interval='* * * * *',  # Schedule the DAG to run every minute
    catchup=False,
)

# Define tasks using PythonOperator
start_task = PythonOperator(
    task_id='start_task',
    python_callable=print_start_message,
    dag=dag,
)

success_task = PythonOperator(
    task_id='success_task',
    python_callable=print_success_message,
    dag=dag,
)

end_task = PythonOperator(
    task_id='end_task',
    python_callable=print_end_message,
    dag=dag,
)

# Set task dependencies
start_task >> success_task >> end_task
