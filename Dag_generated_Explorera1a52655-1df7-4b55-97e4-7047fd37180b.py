from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorera1a52655-1df7-4b55-97e4-7047fd37180b",
}

dag = DAG(
    "Dag_generated_Explorera1a52655-1df7-4b55-97e4-7047fd37180b",
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


op_b3f5e6a97f2a40ae9a5e886851d07d50 = KubernetesPodOperator(
    task_id="b3f5e6a97f2a40ae9a5e886851d07d50",
    name="b3f5e6a97f2a40ae9a5e886851d07d50",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d' --dependencies-archive 'load_data-b3f5e6a97f2a40ae9a5e886851d07d50.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_bd597e77a1c542f69df696e561e6855a = KubernetesPodOperator(
    task_id="bd597e77a1c542f69df696e561e6855a",
    name="bd597e77a1c542f69df696e561e6855a",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d' --dependencies-archive 'Part 1 - Data Cleaning-bd597e77a1c542f69df696e561e6855a.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "f": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_9fb7e6fb879e4ae6bcb5227778cc3801 = KubernetesPodOperator(
    task_id="9fb7e6fb879e4ae6bcb5227778cc3801",
    name="9fb7e6fb879e4ae6bcb5227778cc3801",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d' --dependencies-archive 'Part 3 - Time Series Forecasting-9fb7e6fb879e4ae6bcb5227778cc3801.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/forecasted.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b5dd76cf69df45668d73056842655506 = KubernetesPodOperator(
    task_id="b5dd76cf69df45668d73056842655506",
    name="b5dd76cf69df45668d73056842655506",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d' --dependencies-archive 'Part 2 - Data Analysis-b5dd76cf69df45668d73056842655506.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/datanalysis.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Exploreradc846e2-1331-4994-b44f-5e7b5a853d2d",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b3f5e6a97f2a40ae9a5e886851d07d50 >> op_bd597e77a1c542f69df696e561e6855a

op_bd597e77a1c542f69df696e561e6855a >> op_9fb7e6fb879e4ae6bcb5227778cc3801

op_bd597e77a1c542f69df696e561e6855a >> op_b5dd76cf69df45668d73056842655506
