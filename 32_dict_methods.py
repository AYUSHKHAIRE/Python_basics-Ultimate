ep1 = {1: 34, 2: 43, 3: 44, 4: 50, 5: 11}
print(ep1)
print(type(ep1))
ep2 = {6: 50, 7: 12}
print(ep2)
print(type(ep2))

# updating
ep1.update(ep2)
print(ep1)

# cleaning
ep2.clear()
print(ep2)

# popping
ep1.pop(1)
print(ep1)
ep1.popitem()
print(ep1)

# deleting
del ep2
# print(ep2) # as dict deleted
del ep1[4]
print(ep1)
