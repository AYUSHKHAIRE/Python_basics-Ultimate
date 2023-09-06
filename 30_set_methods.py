s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
s2 = {1, 3, 5, 7, 9, 45, 44, 3}
un = s1.union(s2)
print(un)

unu = s1.intersection_update(s2)
print(unu)

isn = s1.intersection(s2)
print(isn)

# change a value in a set
ch = (s1, s2)
print(ch)
# s1 will updated

# symetric difference
syd = s1.symmetric_difference(s2)
print(syd)

# difference
dff = s2.difference(s1)
print(dff)
