from airflow.sdk import dag, task, chain
from pendulum import datetime


@dag(
    schedule="@daily",
    start_date=datetime(2025, 5, 1),
    tags=["example", "dag_versioning"],
    default_args={
        "owner": "Airflow Korea",
        "retries": 3,
    },
)
def dag_versioning_example():

    @task
    def task_1():
        print("Hello! task_1")

    @task
    def task_2():
        print("Hello! tast_2")
    
    @task
    def task_3():
        print("Hello! tast_3")

    @task
    def task_4():
        print("Hello! tast_4")
    
    chain(
        task_1(),
        task_2(),
        task_3(),
        task_4()
    )


dag_versioning_example()
