# -*- coding: utf-8 -*-

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime
from etl.clear_log_etl import clear_log_file

# -------------------------------------------------------------------------------
# these args will get passed on to each operator
# you can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'yjijn',
    'depends_on_past': False,
    'start_date': datetime.now() + timedelta(hours=-3),
    'email': ['*******@**.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'provide_context': True,  # 设置这参数，kwarg会接受关键字参数
}

# -------------------------------------------------------------------------------
# dag

dag = DAG(
    'dag_clear_log_etl',
    default_args=default_args,
    max_active_runs=1,
    description='定时清理日志文件',
    schedule_interval="00 00 * * *")


# -------------------------------------------------------------------------------
# 清理日志文件

def job_clear_log_file(**kwargs):
    return clear_log_file()

operator_clear_log_file = PythonOperator(
    task_id='task_clear_log_file',
    python_callable=job_clear_log_file,
    dag=dag)

# -------------------------------------------------------------------------------
# dag运行关系
operator_clear_log_file