import configparser
from pyspark import SparkConf


#loading the appication configs in python dictionary
def get_app_config(env):
    config = configparser.ConfigParser()
    config.read("configs/application.conf")
    app_conf = {}
    for (key, val) in config.items(env):
        app_conf[key] = val
    return app_conf


# loading the pyspark config and creating a spark conf object. so that 
# we can pass the same dusring creation of sparkSession
def get_pyspark_config(env):
    config = configparser.ConfigParser()
    config.read("configs/pyspark.conf")
    pyspark_conf = SparkConf()
    for (key, val) in config.items(env):
        pyspark_conf.set(key,val)
    return pyspark_conf