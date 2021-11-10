from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorerd99923c0-69eb-4e95-9e2d-62b2603822b4",
}

dag = DAG(
    "Dag_generated_Explorerd99923c0-69eb-4e95-9e2d-62b2603822b4",
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


op_816a623216e1432bba838724ca27e5c7 = KubernetesPodOperator(
    task_id="816a623216e1432bba838724ca27e5c7",
    name="816a623216e1432bba838724ca27e5c7",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory '' --dependencies-archive 'load_data-816a623216e1432bba838724ca27e5c7.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_7e85f9d7688b48068fb960bb998380ee = KubernetesPodOperator(
    task_id="7e85f9d7688b48068fb960bb998380ee",
    name="7e85f9d7688b48068fb960bb998380ee",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory '' --dependencies-archive 'Part 1 - Data Cleaning-7e85f9d7688b48068fb960bb998380ee.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_b4ddec3dc53841e68c37c2e27a2b6880 = KubernetesPodOperator(
    task_id="b4ddec3dc53841e68c37c2e27a2b6880",
    name="b4ddec3dc53841e68c37c2e27a2b6880",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory '' --dependencies-archive 'Part 3 - Time Series Forecasting-b4ddec3dc53841e68c37c2e27a2b6880.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/forecasted.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_da9a42d5616b49eba170847e0e3de895 = KubernetesPodOperator(
    task_id="da9a42d5616b49eba170847e0e3de895",
    name="da9a42d5616b49eba170847e0e3de895",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint https://storage.googleapis.com --bucket explorer-cloud-storage --directory '' --dependencies-archive 'Part 2 - Data Analysis-da9a42d5616b49eba170847e0e3de895.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/datanalysis.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "s": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_816a623216e1432bba838724ca27e5c7 >> op_7e85f9d7688b48068fb960bb998380ee

op_7e85f9d7688b48068fb960bb998380ee >> op_b4ddec3dc53841e68c37c2e27a2b6880

op_7e85f9d7688b48068fb960bb998380ee >> op_da9a42d5616b49eba170847e0e3de895
