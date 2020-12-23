from Dataframe_samples import dfCars, spark
from pyspark.sql import types as T, functions as F

# SERIALIZING DATA
# convert dataframe to a RDD of json strings, mapped to a RDD of Rows with each row containing a json string, e.g.
#  '{"car_id":1,"name":"Slurp","dob":"1968-03-01","is_green":true,"owner_id":1,"joint_owner_id":2,"car_washer_id":1}'
# then convert rdd to dataframe containing a single column "car_info" (Note: deal with empty rdd to avoid errors)
# DataFrame[car_info: string]

# empty_rdd = dfCars.filter(F.lit("1") == F.lit("0")).toJSON().map(lambda x: T.Row(x))
rdd = dfCars.toJSON().map(lambda x: T.Row(x))
if rdd.isEmpty():
    dfCarsSerialized = spark.createDataFrame([], T.StructType([T.StructField('car_info', T.StringType())]))
else:
    dfCarsSerialized = rdd.toDF(['car_info'])
# print(dfCarsSerialized.collect())
# print(dfCarsSerialized)

# DESERIALIZING DATA
# extract info from dataframe containing column of json strings ('car_info')
# function from_json creates a map ('parsed_car_info') from a supplied schema:
#     key=field name from schema
#     value=json string value corresponding to field name from supplied schema (if found)
#           and then typecast as specified in supplied schema (if castable)
#           if not found or not castable, a null value is returned
schema = dfCars.schema
dfCarsDeserialized = dfCarsSerialized\
    .select(F.from_json(F.col('car_info'), schema).alias('parsed_car_info'))

df1 = dfCarsDeserialized.select(F.col('parsed_car_info.name'))
# print (df1.show())

df2 = dfCarsDeserialized
for field in dfCars.schema.fieldNames():
    df2 = df2.withColumn(field, F.col("parsed_car_info.{}".format(field)))
df2 = df2.drop(F.col('parsed_car_info'))
# print (df2.collect())

schema = T.StructType([
    T.StructField("car_id", T.IntegerType(), True),
    T.StructField("name", T.IntegerType(), True), # if json value can not be cast to integer it returns null
    T.StructField("dob", T.DateType(), True),
    T.StructField("is_blue", T.BooleanType(), True), # if json field not found it returns null
])
dfCarsDeserialized = dfCarsSerialized\
    .select(F.from_json(F.col('car_info'), schema).alias('parsed_car_info'))
# print (dfCarsDeserialized.collect())

df3 = dfCarsDeserialized.select(F.col('parsed_car_info.name'), F.col('parsed_car_info.is_blue'))
# print (df3.show())