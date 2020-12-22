from pyspark.sql import Row, SparkSession, types as T # noqa
from functools import reduce
from Dataframe_samples import dfPersons, dfCars
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

# convert a DataFrame to a list of Row objects using collect function
# [Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
#  Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)]
print('dfPersons.collect() is ...')
# print(dfPersons.collect())

# convert dataframe to a temporary view, queryable via SQL
dfPersons.createOrReplaceTempView('A')
dfAllPeople = spark.sql("select * from A")

# join 2 dataframes together
# join_cond: Column<b'((owner_id = person_id) AND (joint_owner_id = person_id))'>
persons_fk = ['owner_id', 'joint_owner_id']
persons_pk = ['person_id', 'person_id']
join_cond = [
    dfCars[f_key] == dfPersons[p_key]
    for f_key, p_key in zip(persons_fk, persons_pk)
]
join_cond = reduce(lambda x, y: x & y, join_cond)
print('join_cond is ...')
print(join_cond)
dfX = dfCars.join(dfPersons, join_cond, 'left')
# print(dfX.collect())

dfPersons.join(dfPersons, 'person_id', 'left').show()
