from pyspark.sql import Row, SparkSession, types as T
from datetime import date
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

# produce a Dataframe from a list of Row objects (no schema => it is inferred from data)
# DataFrame[id: bigint, name: string, dob: string, chelsea_fan: boolean]
# [Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
#  Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)]
dataA = [
    Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
    Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)
]
dfA = spark.createDataFrame(dataA)
print ('dfA is ...')
print(dfA)
print ('dfA.collect() is ...')
print(dfA.collect())

# produce a Dataframe from a list of Row objects (schema is supplied)
 #DataFrame[id: int, name: string, dob: date, chelsea_fan: boolean]
schema = T.StructType([
    T.StructField("id", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("dob", T.DateType(), True),
    T.StructField("chelsea_fan", T.BooleanType(), True),
])
dataB = [
    Row(id=1, name='Alan', dob=date(1962,11,25), chelsea_fan=True),
    Row(id=2, name='Melanie', dob=date(1963,10,21), chelsea_fan=False)
]
dfB = spark.createDataFrame(dataB, schema)
print ('dfB is ...')
print(dfB)


