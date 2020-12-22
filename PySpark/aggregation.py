from pyspark.sql import Window, functions as F # noqa
from Dataframe_samples import dfCars

# use of parttionBy
w1 = Window.partitionBy('owner_id')
dfX = dfCars.select(['owner_id', 'dob'])\
            .withColumn('max_dob', F.max('dob').over(w1))\
            .filter(F.col('dob') == F.col('max_dob'))\
            .drop('max_dob')\
            .selectExpr('*')
# print(dfX.collect())

# jus select distinct owner_id values
dfX = dfCars.select(['owner_id']).distinct()
print('distinct count ...')
print(dfX.collect())

# determine count of rows per owner_id
dfX = dfCars.select(['owner_id'])\
            .groupby(['owner_id'])\
            .count().withColumnRenamed('count', 'rec_cnt')
print('counts per owner_id ...')
print(dfX.collect())