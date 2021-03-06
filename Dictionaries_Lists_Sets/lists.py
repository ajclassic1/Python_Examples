list_x = []
list_x.append('Junk1') # append a new entry to end of list
list_x.extend(['Alan', 'Peter']) # append new entries from another list
list_x.extend([i for i in range(3)]) # append new entries from a list generated by an iterator
list_x[0] = 'Junk2' # update first entry

for value in list_x:
        print('value = ' + str(value))


# produces list [0, 1, 2, 3]
LIST_A = [i for i in range(4)]
print(LIST_A)

# produces 3 element list [1,2,3]
LIST_B = [i for i in range(1,4)]
print(LIST_B)

# produces 3*1=1 element list list [1,4,9]
LIST_C = [j for i in range(1,4) for j in [i*i]]
print(LIST_C)

# produces 3*3=9 element list [1, 2, 3, 2, 4, 6, 3, 6, 9]
LIST_D = [j for i in range(1,4) for j in [i, 2*i, 3*i]]
print(LIST_D)

# produces 3*1=1 element list ['Alan', 'Melanie', 'Johnson']
names = {1: ["Alan"], 2: ["Melanie"], 3: ["Johnson"]}
LIST_E = [j for i in range(1,4) for j in names[i]]
print(LIST_E)
list_x = []
list_x.append('Junk1') # append a new entry to end of list
list_x.extend(['Alan', 'Peter']) # append new entries from another list
list_x.extend([i for i in range(3)]) # append new entries from a list generated by an iterator
list_x[0] = 'Junk2' # update first entry

for value in list_x:
        print('value = ' + str(value))


# produces list [0, 1, 2, 3]
LIST_A = [i for i in range(4)]
print(LIST_A)

# produces 3 element list [1,2,3]
LIST_B = [i for i in range(1,4)]
print(LIST_B)

# produces 3*1=1 element list list [1,4,9]
LIST_C = [j for i in range(1,4) for j in [i*i]]
print(LIST_C)

# produces 3*3=9 element list [1, 2, 3, 2, 4, 6, 3, 6, 9]
LIST_D = [j for i in range(1,4) for j in [i, 2*i, 3*i]]
print(LIST_D)

# produces 3*1=1 element list ['Alan', 'Melanie', 'Johnson']
names = {1: ["Alan"], 2: ["Melanie"], 3: ["Johnson"]}
LIST_E = [j for i in range(1,4) for j in names[i]]
print(LIST_E)

# converts a list of columns to a string
# SELECT a, b, c
string_x = 'SELECT ' + ', '.join(['a, b, c'])
print(string_x)

# deep copy a list, y: [1, 2, 3]
x = [1,2,3]
y = x[:]
x.append(4)
print(y)

# soft copy a lis (beware if original list changes), y: [1, 2, 3, 4]
x = [1,2,3]
y = x
x.append((4))
print(y)
