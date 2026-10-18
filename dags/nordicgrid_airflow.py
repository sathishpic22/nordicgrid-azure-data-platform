
from datetime import datetime

from airflow.sdk import dag, task


@dag(
    dag_id="nordicgrid_airflow",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["nordicgrid"],
)
def nordicgrid_airflow():

    @task
    def extract():
        print("Extracting Norwegian energy data")
        return {"source": "Elhub", "records": 100}

    @task
    def transform(data):
        print("Transforming energy data")
        return data["records"]

    @task
    def load(records):
        print(f"Successfully processed {records} records")

    load(transform(extract()))


nordicgrid_airflow()

