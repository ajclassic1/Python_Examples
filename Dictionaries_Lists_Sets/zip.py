x = [1,2,3]
y = [4,5,6]

# zip produces a list of tuples, with each tuple taking an element from each lis being zipped
# [(1, 4), (2, 5), (3, 6)]
z = list(zip(x,y))
print(z)
for left_key, right_key in zip(x, y):
    print(left_key + right_key)
