from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688",
}

dag = DAG(
    "Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688",
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


op_34cce5ecffec47839fe6e68612106fcb = KubernetesPodOperator(
    task_id="34cce5ecffec47839fe6e68612106fcb",
    name="34cce5ecffec47839fe6e68612106fcb",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688' --dependencies-archive 'dd-34cce5ecffec47839fe6e68612106fcb.tar.gz' --file '/dd.pl' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "d",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_1bbdbe46a6264f2e8099f5165b187b25 = KubernetesPodOperator(
    task_id="1bbdbe46a6264f2e8099f5165b187b25",
    name="1bbdbe46a6264f2e8099f5165b187b25",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688' --dependencies-archive 'dd-1bbdbe46a6264f2e8099f5165b187b25.tar.gz' --file '/dd.pl' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorera665459a-c444-4afb-9dbc-a08fee6c4688",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_34cce5ecffec47839fe6e68612106fcb >> op_1bbdbe46a6264f2e8099f5165b187b25
