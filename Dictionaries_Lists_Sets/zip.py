from PySpark.Dataframe_samples import dfPersons, dfCars
from pyspark.sql import functions as F
from functools import reduce

x = [1, 2, 3]
y = [4, 5, 6]

# zip produces a list of tuples, with each tuple taking an element from each list being zipped
# [(1, 4), (2, 5), (3, 6)]
l = list(zip(x,y))
print(l)
for left_key, right_key in zip(x, y):
    print(left_key + right_key)

# the list of tuples can be converted into a dictionary of entries
# with keys taken from first list being zipped and values taken from 2nd list
# {1: 4, 2: 5, 3: 6}
d = dict(zip(x,y))
print(d)

# zip can be used when joining 2 dataframes together to get join condition
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

# zip can be used to prefix all columns in a dataframe
# renaming_mapping: {'car_id': 'prefix_car_id', 'name': 'prefix_name', 'dob': 'prefix_dob', ...}
original_column_list = dfCars.columns
renamed_column_list = ['prefix_' + x for x in original_column_list]
renaming_mapping = dict(zip(original_column_list, renamed_column_list))
print(renaming_mapping)
select_expression = [
    F.col(c).alias(renaming_mapping.get(c))
    for c in renaming_mapping
]
dfX = dfCars.select(select_expression)
# print(dfX.collect())
