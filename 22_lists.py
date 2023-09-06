marks=[3,7,8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

set = [1,2,3,4,5,2, 67, "true", True]
print(set)
print(type(set))
print(set[0])
print(set[1])
print(set[2])
print(set[3])

print(set[-3])
print(set[len(set)-3])

if 67 in set:
    print('yes')
else:
    print('no')
print(set)
print(set[:])
print(set[1:])
print(set[:10])
print(set[1:-1])
print(set[1:len(set)-1])
print(set[1:10:2])

# list comprehension
lst = [ i*i for i in range(50)]
print(lst)
lst = [ i*i for i in range(5) if i%2==0]
print(lst)