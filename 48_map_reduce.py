#  my filter reduce


# MAP


def cube(x):
    return x*x*x


print(cube(2))
#  to make cube list of a list
l = [1, 2, 4, 6, 4, 5]
# nl=[]
# for item in l:
#     nl.append(cube(item))
# print(nl)
#  why i should go for too long ?
nl = map(cube, l)
nl = list(map(cube, l))  # for the map
print(nl)
nnl = list(map(lambda x: x*x*x*x, l))  # for the map
print(nnl)


# FILTER
def filt_func(a):
    return a > 4


newl = filter(filt_func, l)
print(newl)
print(list(newl))
#  if it return true then it will show in the output


# REDUCE
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 1+2 =  3+3=6  6+4=10 and so on
sum = reduce(lambda x, y: x+y, numbers)
print(sum)
