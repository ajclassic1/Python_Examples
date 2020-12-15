# converts a list of columns to a string
# SELECT a, b, c
string_x = 'SELECT ' + ', '.join(['a, b, c'])
print(string_x)

# formatting string using %s operator
string_y = "%s FROM A" % string_x
print(string_y)
