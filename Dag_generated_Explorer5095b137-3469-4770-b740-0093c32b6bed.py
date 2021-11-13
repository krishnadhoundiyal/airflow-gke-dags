from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed",
}

dag = DAG(
    "Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed",
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


op_f77bab4aed784defab3fe65be8ed955c = KubernetesPodOperator(
    task_id="f77bab4aed784defab3fe65be8ed955c",
    name="f77bab4aed784defab3fe65be8ed955c",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed' --dependencies-archive 'dd-f77bab4aed784defab3fe65be8ed955c.tar.gz' --file '/dd.pl' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_633a9ce1600640b08e4c008d1b848db3 = KubernetesPodOperator(
    task_id="633a9ce1600640b08e4c008d1b848db3",
    name="633a9ce1600640b08e4c008d1b848db3",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python3 -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed' --dependencies-archive 'dd-633a9ce1600640b08e4c008d1b848db3.tar.gz' --file '/dd.pl' "
    ],
    image="docker.io/amancevice/pandas:1.1.1",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorer5095b137-3469-4770-b740-0093c32b6bed",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_f77bab4aed784defab3fe65be8ed955c >> op_633a9ce1600640b08e4c008d1b848db3
