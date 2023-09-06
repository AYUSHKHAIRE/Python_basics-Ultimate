a=(1,4,7,'hi',True)
print(a)
print(type(a))
b=(9) # this is a intager
#  to make a one elemented touple
c=(8,)
#  cant change a touple
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[-2])
print(a[len(a)-2])

if 7 in a:
    print("7 in touple")
else:
    print('absent')

#  after sloicing it returns a ne wtouple a1
# original will not change 
a1=a[1:3]
print(a1)