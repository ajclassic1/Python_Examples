# produces 4 element list [0, 1, 2, 3]
l = list(range(4))
print(l)

# produces 3 element list [1,2,3]
l = list(range(1,4))
print(l)

# produces 3*3=9 element list [1, 2, 3, 2, 4, 6, 3, 6, 9]
l = [j for i in range(1,4) for j in [i, 2*i, 3*i]]
print(l)