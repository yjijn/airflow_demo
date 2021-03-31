import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta, datetime
from etl.demo_etl import gen_random_data, print_data, rm_etl_temp_file
from utils.utils_etl import gen_json_time

# -------------------------------------------------------------------------------
# these args will get passed on to each operator
# you can override them on a per-task basis during operator initialization

default_args = {
    'owner': 'test',
    'depends_on_past': False,
    'start_date': datetime.now() + timedelta(days=-1),  # 必须大于schedule_interval三倍
    'email': ['123456@qq.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'provide_context': True,  # 设置这参数，kwarg会接受关键字参数
}

# -------------------------------------------------------------------------------
# dag

dag = DAG(
    'dag_demo_etl',
    default_args=default_args,
    max_active_runs=1,
    description='模板dag',
    schedule_interval="00 02 * * *")

# -------------------------------------------------------------------------------
# 获取更新时间段

def job_gen_json_time(**kwargs):
    return gen_json_time()

operator_gen_json_time = PythonOperator(
    task_id='task_gen_json_time',
    python_callable=job_gen_json_time,
    dag=dag)


# -------------------------------------------------------------------------------
# 生成随机数据文件

def job_gen_random_data(**kwargs):
    json_time = kwargs['task_instance'].xcom_pull(task_ids='task_gen_json_time')
    gen_random_data(json_time)
    return json_time

operator_gen_random_data = PythonOperator(
    task_id='task_gen_random_data',
    python_callable=job_gen_random_data,
    dag=dag)

# -------------------------------------------------------------------------------
# 打印数据

def job_print_data(**kwargs):
    json_time = kwargs['task_instance'].xcom_pull(task_ids='task_gen_json_time')
    print_data(json_time)
    return json_time

operator_print_data = PythonOperator(
    task_id='task_print_data',
    python_callable=job_print_data,
    dag=dag)

# -------------------------------------------------------------------------------
# 删除临时文件

def job_rm_etl_temp_file(**kwargs):
    json_time = kwargs['task_instance'].xcom_pull(task_ids='taskGenJsonTime')
    rm_etl_temp_file(json_time)
    return json_time

operator_rm_etl_temp_file = PythonOperator(
    task_id='task_rm_etl_temp_file',
    python_callable=job_rm_etl_temp_file,
    dag=dag)




# -------------------------------------------------------------------------------
# dag运行关系
operator_gen_json_time >> operator_gen_random_data >> operator_print_data >> operator_rm_etl_temp_file
