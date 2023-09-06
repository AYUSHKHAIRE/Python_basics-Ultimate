l = [1, 2, 3, 4, 5, 3, 3, 3, 3]
print(l)

l.append(9)
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)

l.reverse()
print(l)

print(l.index(3))
print(l.count(3))

n = l  # not recommanded . it just a refrence .
n = l.copy()  # use this
n[0] = 11
print(l)

l.insert(1, 566)
print(l)

a = [111, 222, 333]
l.extend(a)
print(l)

q = l+a
print(q)
