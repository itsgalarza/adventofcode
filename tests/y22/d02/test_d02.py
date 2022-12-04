from pyspark.sql import SparkSession
from src.y22.d02 import p1, p2

SAMPLE_DATA = 'tests/y22/d02/samples/input.csv'

def test_run_p1(spark_session: SparkSession):
    res = p1.solver(spark_session, SAMPLE_DATA)
    assert res == 15

def test_run_p2(spark_session: SparkSession): 
    res = p2.solver(spark_session, SAMPLE_DATA)
    assert res == 12