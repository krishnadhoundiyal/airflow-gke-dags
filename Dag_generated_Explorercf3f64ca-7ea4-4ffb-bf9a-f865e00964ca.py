from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
}

dag = DAG(
    "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
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


op_7063929783ad4eb983a537fcba832716 = KubernetesPodOperator(
    task_id="7063929783ad4eb983a537fcba832716",
    name="7063929783ad4eb983a537fcba832716",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca' --dependencies-archive 'load_data-7063929783ad4eb983a537fcba832716.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_e286638691704f85ac84bbcac53cac9e = KubernetesPodOperator(
    task_id="e286638691704f85ac84bbcac53cac9e",
    name="e286638691704f85ac84bbcac53cac9e",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca' --dependencies-archive 'dd-e286638691704f85ac84bbcac53cac9e.tar.gz' --file '/dd.pl' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_4767b66446f14b6381a2e0e71b093b30 = KubernetesPodOperator(
    task_id="4767b66446f14b6381a2e0e71b093b30",
    name="4767b66446f14b6381a2e0e71b093b30",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca' --dependencies-archive 'dd-4767b66446f14b6381a2e0e71b093b30.tar.gz' --file '/dd.pl' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b42b1a4358f743dab563b8edbcb132c4 = KubernetesPodOperator(
    task_id="b42b1a4358f743dab563b8edbcb132c4",
    name="b42b1a4358f743dab563b8edbcb132c4",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca' --dependencies-archive 'someTest-b42b1a4358f743dab563b8edbcb132c4.tar.gz' --file '/someTest.py' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/abc.txt' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "sd",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_4689c7cf884a4ff38b8f0e68103f7bbe = KubernetesPodOperator(
    task_id="4689c7cf884a4ff38b8f0e68103f7bbe",
    name="4689c7cf884a4ff38b8f0e68103f7bbe",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca' --dependencies-archive 'Part 1 - Data Cleaning-4689c7cf884a4ff38b8f0e68103f7bbe.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv;data/noaa-weather-data-jfk-airport/abc.txt;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorercf3f64ca-7ea4-4ffb-bf9a-f865e00964ca",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_7063929783ad4eb983a537fcba832716 >> op_e286638691704f85ac84bbcac53cac9e

op_7063929783ad4eb983a537fcba832716 >> op_4767b66446f14b6381a2e0e71b093b30

op_7063929783ad4eb983a537fcba832716 >> op_b42b1a4358f743dab563b8edbcb132c4

op_e286638691704f85ac84bbcac53cac9e >> op_4689c7cf884a4ff38b8f0e68103f7bbe

op_4767b66446f14b6381a2e0e71b093b30 >> op_4689c7cf884a4ff38b8f0e68103f7bbe

op_b42b1a4358f743dab563b8edbcb132c4 >> op_4689c7cf884a4ff38b8f0e68103f7bbe
