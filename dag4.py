from airflow import DAG
from airflow.utils.dates import days_ago
import os
from airflow import models
from airflow.kubernetes.secret import Secret
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
args = {
    "project_id": "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343"
}

dag = DAG(
    "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343",
    default_args=args,
    start_date=days_ago(1),
    tags=['example2']
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


op_3b7cf0d315bf45ea820ed29ee4687ca7 = KubernetesPodOperator(
    task_id="3b7cf0d315bf45ea820ed29ee4687ca7",
    name="3b7cf0d315bf45ea820ed29ee4687ca7",
    namespace='default',
    cmds=["sh", "-c"],
    arguments=["mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343' --dependencies-archive 'load_data-3b7cf0d315bf45ea820ed29ee4687ca7.tar.gz' --file 'load_data.ipynb' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "DATASET_URL": "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343",
    },
    config_file=None,
    image_pull_policy="Always",

    dag=dag
)

op_29b1d1bae54d48b5b0b3e66cded365ac = KubernetesPodOperator(
    task_id="29b1d1bae54d48b5b0b3e66cded365ac",
    name="29b1d1bae54d48b5b0b3e66cded365ac",
    namespace='default',
    cmds=["sh", "-c"],
    arguments=["mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343' --dependencies-archive 'Part 1 - Data Cleaning-29b1d1bae54d48b5b0b3e66cded365ac.tar.gz' --file 'Part 1 - Data Cleaning.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather.csv' --outputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv'"
    ],
    env_vars={
        "d": "g",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343",
    },
    image="docker.io/amancevice/pandas:1.1.1",
    config_file=None,
    image_pull_policy="Always",
    dag=dag
)

op_3be3433fa22242d1a3fbeeeb7158b571 = KubernetesPodOperator(
    task_id="3be3433fa22242d1a3fbeeeb7158b571",
    name="3be3433fa22242d1a3fbeeeb7158b571",
    namespace='default',
    cmds=["sh", "-c"],
    arguments=["mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343' --dependencies-archive 'Part 3 - Time Series Forecasting-3be3433fa22242d1a3fbeeeb7158b571.tar.gz' --file 'Part 3 - Time Series Forecasting.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv'"
    ],
    env_vars={
        "t": "v",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343",
    },
    image="docker.io/amancevice/pandas:1.1.1",
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_4b4f06f328ff4a788473eb9281948b81 = KubernetesPodOperator(
    task_id="4b4f06f328ff4a788473eb9281948b81",
    name="4b4f06f328ff4a788473eb9281948b81",
    namespace='default',
    cmds=["sh", "-c"],
    arguments=["mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343' --dependencies-archive 'Part 2 - Data Analysis-4b4f06f328ff4a788473eb9281948b81.tar.gz' --file 'Part 2 - Data Analysis.ipynb' --inputs 'data/noaa-weather-data-jfk-airport/jfk_weather_cleaned.csv;data/noaa-weather-data-jfk-airport/jfk_weather.csv'"
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "f",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer2b2e8e29-b074-4907-b4c2-15a15bac17cb4343",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_3b7cf0d315bf45ea820ed29ee4687ca7 >> op_29b1d1bae54d48b5b0b3e66cded365ac

op_29b1d1bae54d48b5b0b3e66cded365ac >> op_4b4f06f328ff4a788473eb9281948b81

op_29b1d1bae54d48b5b0b3e66cded365ac >> op_3be3433fa22242d1a3fbeeeb7158b571
