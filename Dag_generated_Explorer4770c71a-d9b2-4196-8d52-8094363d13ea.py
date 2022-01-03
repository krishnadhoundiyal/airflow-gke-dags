from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
}

dag = DAG(
    "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
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


op_9241a290766e4435ad36942c4f80c76d = KubernetesPodOperator(
    task_id="9241a290766e4435ad36942c4f80c76d",
    name="9241a290766e4435ad36942c4f80c76d",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea' --dependencies-archive 'load_data-9241a290766e4435ad36942c4f80c76d.tar.gz' --file '/load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_8d55bc4281c4473489a356fbc0f3d387 = KubernetesPodOperator(
    task_id="8d55bc4281c4473489a356fbc0f3d387",
    name="8d55bc4281c4473489a356fbc0f3d387",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea' --dependencies-archive 'Part 1 - Data Cleaning-8d55bc4281c4473489a356fbc0f3d387.tar.gz' --file '/Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_1e7dd846e1274db8b4706eab67ddc37d = KubernetesPodOperator(
    task_id="1e7dd846e1274db8b4706eab67ddc37d",
    name="1e7dd846e1274db8b4706eab67ddc37d",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea' --dependencies-archive 'Part 2 - Data Analysis-1e7dd846e1274db8b4706eab67ddc37d.tar.gz' --file '/Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_42aed7f0bcb444b89b6702c0efa46084 = KubernetesPodOperator(
    task_id="42aed7f0bcb444b89b6702c0efa46084",
    name="42aed7f0bcb444b89b6702c0efa46084",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea' --dependencies-archive 'Part 3 - Time Series Forecasting-42aed7f0bcb444b89b6702c0efa46084.tar.gz' --file '/Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer4770c71a-d9b2-4196-8d52-8094363d13ea",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_9241a290766e4435ad36942c4f80c76d >> op_8d55bc4281c4473489a356fbc0f3d387

op_8d55bc4281c4473489a356fbc0f3d387 >> op_1e7dd846e1274db8b4706eab67ddc37d

op_8d55bc4281c4473489a356fbc0f3d387 >> op_42aed7f0bcb444b89b6702c0efa46084
