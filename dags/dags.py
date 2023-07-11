import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from operators import first_operator, second_operator


with DAG(
    dag_id="main_dag",
    schedule_interval="@hourly",
    default_args={
        "owner": "airflow",
        "retries": 3,
        "retry_delay": datetime.timedelta(minutes=5),
        "start_date": datetime.datetime.utcnow(),
    },
    catchup=False
) as f:

    first_operator_execution = PythonOperator(
        task_id="first_operator_execution",
        python_callable=first_operator,
        provide_context=True,
        op_kwargs={"name": "Mehdi Samsami"}
    )

    second_operator_execution = PythonOperator(
        task_id="second_operator_execution",
        python_callable=second_operator,
        provide_context=True,
    )

first_operator_execution >> second_operator_execution
