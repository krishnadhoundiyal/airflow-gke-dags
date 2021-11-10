from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
}

dag = DAG(
    "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
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


op_9820b4f15f8749169e2a6a5545f5e865 = KubernetesPodOperator(
    task_id="9820b4f15f8749169e2a6a5545f5e865",
    name="9820b4f15f8749169e2a6a5545f5e865",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint orage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242' --dependencies-archive 'load_data-9820b4f15f8749169e2a6a5545f5e865.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_62c60e21fe3c4781b58a5e68ee0705f4 = KubernetesPodOperator(
    task_id="62c60e21fe3c4781b58a5e68ee0705f4",
    name="62c60e21fe3c4781b58a5e68ee0705f4",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint orage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242' --dependencies-archive 'Part 1 - Data Cleaning-62c60e21fe3c4781b58a5e68ee0705f4.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "s": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_47400a3a3c68463abacd3e0554979f08 = KubernetesPodOperator(
    task_id="47400a3a3c68463abacd3e0554979f08",
    name="47400a3a3c68463abacd3e0554979f08",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint orage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242' --dependencies-archive 'Part 3 - Time Series Forecasting-47400a3a3c68463abacd3e0554979f08.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/forecasted.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "f": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_90dc81087b9945a99cf2c067a9e87d74 = KubernetesPodOperator(
    task_id="90dc81087b9945a99cf2c067a9e87d74",
    name="90dc81087b9945a99cf2c067a9e87d74",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint orage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242' --dependencies-archive 'Part 2 - Data Analysis-90dc81087b9945a99cf2c067a9e87d74.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/datanalysis.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "s": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer8350e627-6108-4024-a634-801a08626242",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_9820b4f15f8749169e2a6a5545f5e865 >> op_62c60e21fe3c4781b58a5e68ee0705f4

op_62c60e21fe3c4781b58a5e68ee0705f4 >> op_47400a3a3c68463abacd3e0554979f08

op_62c60e21fe3c4781b58a5e68ee0705f4 >> op_90dc81087b9945a99cf2c067a9e87d74
