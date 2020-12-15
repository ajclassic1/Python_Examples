from pyspark.sql import Row, SparkSession, types as T, functions as F
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

# create a Dataframe from a list of Row objects
# DataFrame[id: bigint, name: string]
schema = T.StructType([
    T.StructField("id", T.IntegerType(), True),
    T.StructField("name", T.StringType(), True),
])
dataA = [
    Row(id=1, name='Alan'),
    Row(id=2, name='Alanxxx'),
    Row(id=3, name='xxxAlan'),
    Row(id=4, name='xxxAlanxxx'),
    Row(id=5, name='xxxAla'),
    Row(id=6, name='alanPeter'),
    Row(id=7, name='AlanxxxPeter'),
    Row(id=8, name='Alan_xxx'),
    Row(id=9, name='xxx_Peter'),
    Row(id=10, name='xxx'),
]
dfA = spark.createDataFrame(dataA, schema)
print('dfA is ...')
print(dfA)

# filter to get only rows where Alan or Peter exist in the name field
dfB = dfA.select(F.col("id"), F.col("name"), F.regexp_extract(F.col("name"), '.*(Alan|Peter).*', 1).alias('match'))\
         .filter(F.col('match') != '')
print('dfB is ...')
print(dfB.collect())
