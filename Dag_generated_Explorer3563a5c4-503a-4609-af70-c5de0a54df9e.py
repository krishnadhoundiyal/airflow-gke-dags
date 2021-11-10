from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorer3563a5c4-503a-4609-af70-c5de0a54df9e",
}

dag = DAG(
    "Dag_generated_Explorer3563a5c4-503a-4609-af70-c5de0a54df9e",
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


op_682578aba37f4009a84135bd30e2e1b3 = KubernetesPodOperator(
    task_id="682578aba37f4009a84135bd30e2e1b3",
    name="682578aba37f4009a84135bd30e2e1b3",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8' --dependencies-archive 'load_data-682578aba37f4009a84135bd30e2e1b3.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_e8fb1680ab3b4abaa6df4dedb8317f55 = KubernetesPodOperator(
    task_id="e8fb1680ab3b4abaa6df4dedb8317f55",
    name="e8fb1680ab3b4abaa6df4dedb8317f55",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8' --dependencies-archive 'Part 1 - Data Cleaning-e8fb1680ab3b4abaa6df4dedb8317f55.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "c",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_87dcc12a02a1416db70b26be6c07e04d = KubernetesPodOperator(
    task_id="87dcc12a02a1416db70b26be6c07e04d",
    name="87dcc12a02a1416db70b26be6c07e04d",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8' --dependencies-archive 'Part 3 - Time Series Forecasting-87dcc12a02a1416db70b26be6c07e04d.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/forecasted.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_8774d5a703494b3582e6352704d9cab9 = KubernetesPodOperator(
    task_id="8774d5a703494b3582e6352704d9cab9",
    name="8774d5a703494b3582e6352704d9cab9",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8' --dependencies-archive 'Part 2 - Data Analysis-8774d5a703494b3582e6352704d9cab9.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/datanalysis.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "dd",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer414cdbae-94ea-4026-aeb8-35304ac096f8",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_682578aba37f4009a84135bd30e2e1b3 >> op_e8fb1680ab3b4abaa6df4dedb8317f55

op_e8fb1680ab3b4abaa6df4dedb8317f55 >> op_87dcc12a02a1416db70b26be6c07e04d

op_e8fb1680ab3b4abaa6df4dedb8317f55 >> op_8774d5a703494b3582e6352704d9cab9
