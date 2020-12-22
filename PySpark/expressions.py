from pyspark.sql import functions as F # noqa
from PySpark.Dataframe_samples import dfCars

dfX = dfCars.select('name', 'owner_id', 'car_washer_id')
dfX = dfCars.select('name', *['owner_id', 'car_washer_id'])

# use & or | or ==
dfX = dfCars.withColumn('col_a', (F.col('owner_id') == F.lit(1)) & (F.col('car_washer_id') == F.lit(1)))\
            .withColumn('col_b', (F.col('owner_id') == F.lit(1)) | (F.col('car_washer_id') == F.lit(1)))\
            .withColumn('col_c', (F.isnull(F.col('owner_id'))) | (F.col('car_washer_id') == F.lit(1)))\
            .withColumn('col_d', (F.isnull(F.col('owner_id'))) | (F.col('car_washer_id') == F.lit(1)))\
            .selectExpr('name as car_name', 'col_a', 'col_b')
# print(dfX.collect())

# nulls
dfX = dfCars.withColumn('col_a',F.when(F.isnull(F.col('owner_id')), F.lit(True)).otherwise(F.lit(False)))\
            .withColumn('col_b',F.when(F.col('owner_id').isNull(), F.lit(True)).otherwise(F.lit(False)))\
            .withColumn('col_c',F.when(F.col('owner_id').isNotNull(), F.lit(True)).otherwise(F.lit(False)))\
            .selectExpr('col_a', 'col_b', 'col_c')
# print(dfX.collect())

dfX = dfCars.filter(F.expr("dob = DATE('1968-09-11')"))\
            .filter(F.col('dob') == F.lit('1968-09-11'))
# print(dfX.collect())

x = ['car_id', 'name']
y = [F.col('car_id'), F.lit('-'), F.lit(None), F.col('name')]
dfX = dfCars.withColumn('col_a', F.concat_ws('', F.col('car_id'), F.lit('-'), F.lit(None), F.col('name')))\
            .withColumn('col_b', F.concat_ws('', *x))\
            .withColumn('col_c', F.concat_ws('', *y))\
            .selectExpr('col_a', 'col_b', 'col_c')
print(dfX.collect())