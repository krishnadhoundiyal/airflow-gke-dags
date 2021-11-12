from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a",
}

dag = DAG(
    "Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a",
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


op_1cbfde2afffc4047a2c791f213faa740 = KubernetesPodOperator(
    task_id="1cbfde2afffc4047a2c791f213faa740",
    name="1cbfde2afffc4047a2c791f213faa740",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a' --dependencies-archive 'someTest-1cbfde2afffc4047a2c791f213faa740.tar.gz' --file '/someTest.py' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/abc.txt' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "w",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b594bcd082874019a329bf9c35fc2975 = KubernetesPodOperator(
    task_id="b594bcd082874019a329bf9c35fc2975",
    name="b594bcd082874019a329bf9c35fc2975",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a' --dependencies-archive 'load_data-b594bcd082874019a329bf9c35fc2975.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerc36ce611-9b25-42b2-bf14-5367aca4dc8a",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b594bcd082874019a329bf9c35fc2975 >> op_1cbfde2afffc4047a2c791f213faa740
