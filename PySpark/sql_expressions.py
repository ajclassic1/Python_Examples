from pyspark.sql import SparkSession
from PySpark.Dataframe_samples import dfCars
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

dfCars.createGlobalTempView('cars')
dfX = spark.sql(
    'SELECT name, owner_id FROM global_temp.cars cars '
    'WHERE owner_id=1 AND car_washer_id = 1'
)
# print(dfX.collect())

dfY = spark.sql(
    """
    SELECT name AS car_name, owner_id FROM global_temp.cars cars
    WHERE owner_id=1 AND car_washer_id = 1
    AND dob != DATE('1968-09-11')
    """
)
print(dfY.collect())
