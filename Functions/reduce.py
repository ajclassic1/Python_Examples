from functools import reduce
from pyspark.sql import functions as F
from PySpark.Dataframe_samples import dfCars

# adds the elements of a list together: (1 + 2 + 3)
x = reduce(lambda x, y: x + y, [1, 2, 3])
print(x)

# finds maximum of list: 7
x = reduce(lambda x, y: x if x > y else y, [1, 7, 3, 4])
print(x)

# concatenates columns of a dataframe: Column<b'concat(concat(owner_id, joint_owner_id), car_washer_id)'>
x = reduce(lambda x, y: F.concat(x,y), [dfCars['owner_id'], dfCars['joint_owner_id'], dfCars['car_washer_id']])
print(x)
