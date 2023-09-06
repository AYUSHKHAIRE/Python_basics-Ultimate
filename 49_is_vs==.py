a = 4
b = '4'
print(a == b)
print(a is b)  # compare for exact location of objects in memory

# is and == both are comparision operators
a = [1, 3, 55]
b = [1, 3, 55]
print(a == b)
print(a is b)

a = 4  # it is know to python that is a constant.it dont waste a new memory location
b = 4  # means now a and b will point to same memory locatyion where there is 3 kept
print(a == b)
print(a is b)

a = 'ayush'
b = 'ayush'
print(a == b)
print(a is b)

a = (4, 5, 6)
b = (4, 5, 6)
print(a == b)
print(a is b)

a = None
b = None
print(a == b)  # compare value
print(a is b)  # compare identity
print(a is None)
