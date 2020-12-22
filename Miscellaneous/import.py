# from PySpark.Dataframe_samples import dfCars
import importlib
from importlib import import_module
from inspect import getmembers

# if whole module is imported, need to mention module name with very use
# x is a list of tuples - the first element of each tuple may be a function name that exists in that module
# the second element of each tuple may be the actual function that exists in that module
imported_module_1 = importlib.import_module('PySpark.Dataframe_samples')
x = getmembers(imported_module_1)
print('1st module has members ...')
print(x)

# if only an element from module is imported, module name does not need to be specified
imported_module_2 = import_module('Functions.reduce')
x = getmembers(imported_module_2)
print('2nd module has members ...')
print(x)
