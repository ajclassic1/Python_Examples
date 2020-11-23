from pyspark.sql import Row, SparkSession, types as T
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

# produce a Dataframe from a list of Row objects
# DataFrame[id: bigint, name: string, dob: string, chelsea_fan: boolean]
dataA = [
    Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
    Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)
]
dfA = spark.createDataFrame(dataA)
print ('dfA is ...')
print(dfA)

# [Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
#  Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)]
print ('dfA.collect() is ...')
print(dfA.collect())
