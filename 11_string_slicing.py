a = "ayushkhaire"
# shortlisting charactors
# index starts as 0  1  2  3  4 ...
print(a[0:4])
# length 
print(len(a))
print(a[:3])
# from this to this 
print(a[1:4])
print(a[:])
print(a[0:-4])
print(a[:len(a)-4])  # same
print(a[-1::len(a)-4]) 
print(a[-1 : -3])
nm = "harry"
print(nm[-4:-2])