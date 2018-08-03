from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta

#Default args

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2018, 1, 8),
    'email': ['fauzia@qbizinc.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

#create a DAG object by passing-DAG name,default arguments and schedule interval

dag=DAG('simple_dag',default_args=default_args,schedule_interval=timedelta(5))
t1=BashOperator(
	task_id="first_script",
	bash_command="/home/ec2-user/airflow/dags/first_script.sh ",retries=1,
	dag=dag)

t2=BashOperator(
	task_id="second_script",
	bash_command="/home/ec2-user/airflow/dags/second_script.sh ",retries=1,
	dag=dag)

t2.set_upstream(t1)
