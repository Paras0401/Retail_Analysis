import pytest
from lib.Utils import get_spark_session


# @pytest.fixture
# def spark():
#     spark_se =  get_spark_session("LOCAL")
#     return spark_se

##to return the resources we need to modify the above code as below

@pytest.fixture
def spark():
    "create saprk session"
    spark_se =  get_spark_session("LOCAL")
    yield spark_se
    spark_se.stop()

@pytest.fixture
def expected_results(spark):
    "give the expected result"
    result_schema = 'state string, count int'
    return spark.read.format("csv").schema(result_schema).load("data/test_result/state_aggregate.csv")