from airflow import DAG
from airflow.utils.dates import days_ago
from airflow import models
import os
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow.kubernetes.secret import Secret


args = {
    "project_id": "Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391",
}

dag = DAG(
    "Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391",
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


op_81d0a223f9404b6081e5822e5b4e0608 = KubernetesPodOperator(
    task_id="81d0a223f9404b6081e5822e5b4e0608",
    name="81d0a223f9404b6081e5822e5b4e0608",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391' --dependencies-archive 'dd-81d0a223f9404b6081e5822e5b4e0608.tar.gz' --file '/dd.pl' "
    ],
    image="ericssonkubernetes/perl-python3-curl",
    env_vars={
        "d": "s",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_de897ebc7f484702ad3a8deec6120a0f = KubernetesPodOperator(
    task_id="de897ebc7f484702ad3a8deec6120a0f",
    name="de897ebc7f484702ad3a8deec6120a0f",
    namespace="default",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/runnotebook.py --output runnotebook.py && curl -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/krishnadhoundiyal/explorer/main/requirements-explorer.txt --output requirements.txt && python3 -m pip install packaging && python -m pip install -r requirements.txt && python3 -m pip freeze > requirements-current.txt && python3 runnotebook.py --endpoint storage.googleapis.com --bucket explorer-cloud-storage --directory 'Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391' --dependencies-archive 'dd-de897ebc7f484702ad3a8deec6120a0f.tar.gz' --file '/dd.pl' "
    ],
    image="ericssonkubernetes/perl-python3-curl",
    env_vars={
        "": "",
        "RUNTIME_ENV": "NotebookOp",
        "AWS_ACCESS_KEY_ID": "GOOGL5U4Z4PN6BCIYVZRQPIZ",
        "AWS_SECRET_ACCESS_KEY": "0PKhq1+tiY89IzXwwhF5MqXTYefFCfZl8mksiqe8",
        "EXPLORER_RUN_NAME": "Dag_generated_Explorerfde126d8-7313-4a60-9637-1f228d64a391",
    },
    config_file=None,
    image_pull_policy="Always",
    dag=dag,
)

op_81d0a223f9404b6081e5822e5b4e0608 >> op_de897ebc7f484702ad3a8deec6120a0f
