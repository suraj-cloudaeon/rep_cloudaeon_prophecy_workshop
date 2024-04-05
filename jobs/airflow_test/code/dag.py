import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow import DAG
from airflow.models.param import Param
from airflow.decorators import task
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from s15rijrgbhifo6uxfcytiq_.tasks import Pipeline_0
PROPHECY_RELEASE_TAG = "__PROJECT_ID_PLACEHOLDER__/__PROJECT_RELEASE_VERSION_PLACEHOLDER__"

with DAG(
    dag_id = "S15rIJRGbhIfO6UxfCYtiQ_", 
    schedule_interval = "0/15 * * * *", 
    default_args = {
      "owner": "Prophecy", 
      "email": "sharad.ghallal@cloudaeon.net", 
      "email_on_failure": True, 
      "email_on_retry": True, 
      "ignore_first_depends_on_past": True, 
      "do_xcom_push": True, 
      "pool": "hrlFHyu4"
    }, 
    start_date = pendulum.today('UTC'), 
    end_date = pendulum.datetime(2024, 4, 10, tz = "UTC"), 
    catchup = True, 
    tags = []
) as dag:
    Pipeline_0_op = Pipeline_0()
