from PySpark.Dataframe_samples import dfCars

# converts a list of columns to a string
# "SELECT a, b, c"

string_x = 'SELECT ' + ', '.join(['a, b, c'])
print(string_x)

# formatting string using %s operator
# "SELECT a, b, c FROM A"
string_y = "%s FROM A" % string_x
print(string_y)

# formatting string using {}
# "SELECT a, b, c FROM B"
string_z = "{} FROM B".format(string_x)
print(string_z)

# takes 1st 3 characters from a string
# dhc
x = 'dhcs_xxx'
print(x[0:3])

# print('dfCars: {}'.format(dfCars.collect()))
# print('dfCars: {}'.format(dfCars.show()))
print(dfCars.show())
