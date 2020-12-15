from pyspark.sql import Row, SparkSession, types as T # noqa
from datetime import date
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

# dfPersons (used in examples)
# produce a Dataframe from a list of Row objects (schema is supplied)
# DataFrame[people_id: int, name: string, dob: date, chelsea_fan: boolean]
schema = T.StructType([
    T.StructField("person_id", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("dob", T.DateType(), True),
    T.StructField("chelsea_fan", T.BooleanType(), True),
])
data = [
    Row(person_id=1, name='Alan', dob=date(1962, 11, 25), chelsea_fan=True),
    Row(person_id=2, name='Melanie', dob=date(1963, 10, 21), chelsea_fan=False)
]
dfPersons = spark.createDataFrame(data, schema)

# dfCars
schema = T.StructType([
    T.StructField("car_id", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
    T.StructField("dob", T.DateType(), True),
    T.StructField("is_green", T.BooleanType(), True),
    T.StructField("owner_id", T.IntegerType(), True),
    T.StructField("joint_owner_id", T.IntegerType(), True),
    T.StructField("car_washer_id", T.IntegerType(), True),
])
data = [
    Row(car_id=1, name='Slurp', dob=date(1968, 3, 1), is_green=True,
        owner_id=1, joint_owner_id=2, car_washer_id=1),
    Row(car_id=2, name='Mavis', dob=date(1968, 9, 11), is_green=False,
        owner_id=2, joint_owner_id=1, car_washer_id=1)
]
dfCars = spark.createDataFrame(data, schema)
