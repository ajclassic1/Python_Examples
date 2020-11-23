from pyspark.sql import Row, SparkSession, types as T

# create a Row object using 1st method (using name=value)
# Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True)
row_x = Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True)
print(row_x)

# create a Row object using 2nd method (using row factory)
# Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)
user_row = Row("id", "name", "dob", "chelsea_fan")
row_x = user_row(2, 'Melanie', '1963-10-21', False)
print(row_x)

# create a list of Row objects using 1st method (using name=value)
# [Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
#  Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)]
dataA = [
    Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
    Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)
]
print('dataA is ...')
print(dataA)

# create a list of Row objects using 2nd method (using row factory)
# [Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True),
#  Row(id=2, name='Melanie', dob='1963-10-21', chelsea_fan=False)]
user_row = Row("id", "name", "dob", "chelsea_fan")
dataB = [
    user_row(1, 'Alan', '1962-11-25', True),
    user_row(2, 'Melanie', '1963-10-21', False)
]
print('dataB is ...')
print(dataB)

########################################

row_x = Row(id=1, name='Alan', dob='1962-11-25', chelsea_fan=True)

# create a list of field values from a Row object using the list function
# [1, 'Alan', '1962-11-25', True]
print('List of row field values is ...')
print(list(row_x))

# create a dictionary of field names/values from a Row object using the asDict method
# {'id': 1, 'name': 'Alan', 'dob': '1962-11-25', 'chelsea_fan': True}
print('Dictionary of row field names/values is ...')
print(row_x.asDict())

# create a list of field values from a Row object using the list() function or asDict.values() method function
# [1, 'Alan', '1962-11-25', True]
print('List of row field values is ...')
print(list(row_x))
print(list(row_x.asDict().values()))

# a field value can be obtained from a row by one of 2 methods
# 'Alan'
# 'Alan'
print('A row field values is ...')
print(row_x['name'])
print(row_x.name)

# the presence of a field name in a row can be determened using in
# True
print('dob' in row_x)