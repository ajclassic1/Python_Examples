# prints 1, 2, 3, and 4
for i in [1, 2, 3, 4]:
    print(i)

# prints 2, 3, and 4
for i in [x for x in [1, 2, 3, 4] if x >= 2]:
    print(i)

x = 1
if x == 1:
    print('Alan')
elif x==2:
    print('Peter')
else:
    print('Johnson')
