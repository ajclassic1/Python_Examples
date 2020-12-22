from itertools import chain

# ['A', 'l', 'a', 'n', 'P', 'e', 't', 'e', 'r']
# function has only 1 argument, so argument is interpreted as a list of iterables
# the 1st iterable is the string!!!! ('Alan')
# the 2nd iterable is the strin!!! ('Peter')
# function returns elements from 1st iterable till it is exausted: A', 'l', 'a', 'n'
# function returns elements from 2nd iterable till it is exausted: 'P', 'e', 't', 'e', 'r'
# None is not iterable so can not include tuple (None)
sorted_x = chain.from_iterable([('Alan'), ('Peter')])
print('sorted_x is ...')
print(list(sorted_x))

# [True, 'Alan', True, 'Peter', False, None]
# function has only 1 argument, so argument is interpreted as a list of iterables
# the 1st iterable is the 2-element tuple (True, 'Alan')
# the 2nd iterable is the 2-element tuple (True, 'Peter')
# the 3rd iterable is the 2-element tuple (False, None)
# function returns elements from 1st iterable till it is exausted: True, 'Alan'
# function returns elements from 2nd iterable till it is exausted: True, 'Peter'
# function returns elements from 3rd iterable till it is exausted: False, None
sorted_x = chain.from_iterable([(True, 'Alan'), (True, 'Peter'), (False, None)])
print('sorted_x is ...')
print(list(sorted_x))