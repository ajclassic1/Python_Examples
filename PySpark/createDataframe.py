from pyspark.sql import Row, SparkSession, types as T # noqa
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
print('dfA is ...')
print(dfA)
print('dfA.collect() is ...')
print(dfA.collect())

# produce a Dataframe from a list of Row objects (schema is supplied)
# schema has 3rd argument saying if field can contain nulls
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
dfPersons1 = spark.createDataFrame(data, schema)
print('dfPersons1 is ...')
print(dfPersons1)

# produce a Dataframe from a list of Dictionaries (schema is supplied)
# DataFrame[people_id: int, name: string, dob: date, chelsea_fan: boolean]
schema = T.StructType([
    T.StructField("person_id", T.IntegerType()),
    T.StructField("name", T.StringType()),
    T.StructField("dob", T.DateType()),
    T.StructField("chelsea_fan", T.BooleanType()),
])
data = [
    {'person_id': 1, 'name': 'Alan', 'dob': date(1962, 11, 25), 'chelsea_fan': True},
    {'person_id': 2, 'name': 'Melanie', 'dob': date(1963, 10, 21), 'chelsea_fan': False}
]
dfPersons2 = spark.createDataFrame(data, schema)
print('dfPersons2 is ...')
print(dfPersons2.show())
print(dfPersons2.schema)
