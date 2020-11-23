from pyspark.sql import Row, SparkSession, types as T
from collections import defaultdict
spark = SparkSession.builder.config("spark.some.config.option", "config-value").getOrCreate()

###############################################

dataA = [
    Row(country_id='CH', bu='0001', country_cnt=1000, error_cnt=100),
    Row(country_id='CH', bu='0002', country_cnt=500, error_cnt=50),
    Row(country_id='MX', bu='0003', country_cnt=100, error_cnt=10),
    Row(country_id='MX', bu='0004', country_cnt=50, error_cnt=5)
]
dfA = spark.createDataFrame(dataA)

# collect returns a list of rows
# [Row(country_id='CH', bu='0001', country_cnt=1000, error_cnt=100),
#  Row(country_id='CH', bu='0002', country_cnt=500, error_cnt=50),
#  Row(country_id='MX', bu='0003', country_cnt=100, error_cnt=10),
#  Row(country_id='MX', bu='0004', country_cnt=50, error_cnt=5)]
x = dfA.collect()
print('x is ...')
print(x)

# create a list of lists (1 list per row containing just the field values for that row)
# [['CH', '0001', 1000, 100], ['CH', '0002', 500, 50], ['MX', '0003', 100, 10], ['MX', '0004', 50, 5]]
y = [list(row) for row in dfA.collect()]
print('y is ...')
print(y)

# creates a dictionary from above
# where the key is the country (taken from the 1st field value of each row)
# and the value is a list of lists (1 list per row containing the remaining field values for that row)
# {'CH': [['0001', 1000, 100], ['0002', 500, 50]], 'MX': [['0003', 100, 10], ['0004', 50, 5]]}
dict_x = defaultdict(list)
y = [list(row) for row in dfA.collect()]
for item in y:
    dict_x[item[0]].append(item[1:])
print('dict_x = ...')
print(dict_x)

# as above, but creates a dictionary
# where the key is the country (taken from the 1st field value of each row)
# and the value is a tuple of lists (1 list per row containing the remaining field values for that row)
# {'CH': (['0001', 1000, 100], ['0002', 500, 50]), 'MX': (['0003', 100, 10], ['0004', 50, 5])}
z = dict((key, tuple(value)) for key, value in dict_x.items())
print ('z is ...')
print(z)

# create a new directory, where the 2nd field of each row (business_unit) becomes a key
# {'CH': {'business_unit': {'0001': {'total_cnt': 1000, 'err_cnt': 100}, '0002': {'total_cnt': 500, 'err_cnt': 50}}},
#  'MX': {'business_unit': {'0003': {'total_cnt': 100, 'err_cnt': 10}, '0004': {'total_cnt': 50, 'err_cnt': 5}}}
# }
message_per_country_bu_dict = {
    country_id: {
        'business_unit': {
            k[0]: {
                'total_cnt': k[1],
                'err_cnt': k[2]
            } for k in z[country_id]
        }
    } for country_id in z
}
print('message_per_country_bu_dict is ...')
print(message_per_country_bu_dict)

###############################################

dataB = [
    Row(country_id='CH', country_cnt=1000, error_cnt=100),
    Row(country_id='MX', country_cnt=500, error_cnt=50),
]
dfB = spark.createDataFrame(dataB)

# create a list of lists (1 list per row containing just the field values for that row)
# [['CH', 1000, 100], ['MX', 500, 50]]
y = [list(row) for row in dfB.collect()]
print('y is ...')
print(y)

# create a new directory, where the 1st field of each row (country_id) becomes a key
# and the other fields are used to build the value
# {'CH': {'total_cnt': 1000, 'err_cnt': 100}, 'MX': {'total_cnt': 500, 'err_cnt': 50}}
message_per_country_dict = {
    item[0]: {
            'total_cnt': item[1],
            'err_cnt': item[2]
    } for item in [list(row) for row in dfB.collect()]
}
print('message_per_country_dict is ...')
print(message_per_country_dict)

# message_per_country_dict.values.tolist()
