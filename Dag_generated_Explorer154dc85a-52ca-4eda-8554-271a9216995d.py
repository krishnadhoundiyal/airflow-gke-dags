from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d",
}

dag = DAG(
    "Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Take This from User",
    is_paused_upon_creation=False,
)


# Ensure that the secret named '0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8' is defined in the Kubernetes namespace where this pipeline will be run
env_var_secret_id = Secret(
    deploy_type="env",
    deploy_target="AWS_ACCESS_KEY_ID",
    secret="0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
    key="AWS_ACCESS_KEY_ID",
)
env_var_secret_key = Secret(
    deploy_type="env",
    deploy_target="AWS_SECRET_ACCESS_KEY",
    secret="0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
    key="AWS_SECRET_ACCESS_KEY",
)


op_1b23dd994acc452b877faaaeaa3646ce = KubernetesPodOperator(
    task_id="1b23dd994acc452b877faaaeaa3646ce",
    name="1b23dd994acc452b877faaaeaa3646ce",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d' --dependencies-archive 'load_data-1b23dd994acc452b877faaaeaa3646ce.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_d1a42e99557d4f3ab614974c6405ff41 = KubernetesPodOperator(
    task_id="d1a42e99557d4f3ab614974c6405ff41",
    name="d1a42e99557d4f3ab614974c6405ff41",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d' --dependencies-archive 'Part 1 - Data Cleaning-d1a42e99557d4f3ab614974c6405ff41.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer154dc85a-52ca-4eda-8554-271a9216995d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_1b23dd994acc452b877faaaeaa3646ce >> op_d1a42e99557d4f3ab614974c6405ff41
