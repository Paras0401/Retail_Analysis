from lib.DataReader import read_customers, read_orders
from lib.DataManipulation import filter_closed_orders, count_orders_state, filter_orders_generic
from lib.ConfigReader import get_app_config
import pytest

@pytest.mark.skip() 
def test_read_customers_df(spark):
    customers_count = read_customers(spark,"LOCAL").count()
    assert customers_count == 12435

@pytest.mark.skip() 
def test_read_orders_df(spark):
    orders_count = read_orders(spark,"LOCAL").count()
    assert orders_count == 68884


@pytest.mark.skip() 
# @pytest.mark.transformation()      #transfrmation is given by us. we can give any name
def test_filter_closed_orders(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_closed_orders(orders_df).count()
    assert filtered_count == 7556

@pytest.mark.skip() 
def test_raad_app_config():
    config = get_app_config("LOCAL")
    assert config["orders.file.path"] == "data/orders.csv"

# @pytest.mark.slow()
@pytest.mark.skip()
def test_count_orders_state(spark,expected_results):   # expected_results is a fixture
    customers_df = read_customers(spark, "LOCAL")
    actual_result = count_orders_state(customers_df)
    # assert actual_result.collect() == expected_results.collect()

    # we need to sort the results otherwise it will throw error.
    # assert actual_result.collect().sort() == expected_results.collect().sort()
    # df.sort will sort and return null so according to above line none==none which is always true 
    # so wvwn we change the data state_aggregate file the still it always pass. so we need to write 
    # sorted.
    assert sorted(actual_result.collect()) == sorted(expected_results.collect())


#testing for test cases "filter_orders_generic"
@pytest.mark.skip()
# @pytest.mark.latest()
def test_check_closed_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_orders_generic(orders_df,"CLOSED").count()
    assert filtered_count == 7556

@pytest.mark.skip()
# @pytest.mark.latest()
def test_check_pending_payments_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_orders_generic(orders_df,"PENDING_PAYMENT").count()
    assert filtered_count == 15030

@pytest.mark.skip()
# @pytest.mark.latest()
def test_check_complete_count(spark):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_orders_generic(orders_df,"COMPLETE").count()
    assert filtered_count == 22900

# in the above 3 test cases there is lot of redundency as we need to changing values (count and status) manually. Instead of it we can parameterized it so it will become only 1 function. 


#let's create parametized function for test
@pytest.mark.parametrize(
        "status,count",
        [("CLOSED", 7556),
         ("PENDING_PAYMENT", 15030),
         ("COMPLETE", 22900)]
)
def test_check_count(spark,status,count):
    orders_df = read_orders(spark,"LOCAL")
    filtered_count = filter_orders_generic(orders_df,status).count()
    assert filtered_count == count