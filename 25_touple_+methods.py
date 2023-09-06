vars = ('a','b','c','d','e','f','g','h')
print(vars)

temp=list(vars)
print(temp)

temp.append('z') # add item
print(temp)

temp.pop(3) # remiove item
print(temp)

temp[2]='y' # change item
print(temp)

vars = tuple(temp)
print(vars)

vars1=('v','w','x','y','z')
total = vars+vars1 # concactinate
print(total)

print(vars.count('z'))

print(vars.index('z'))
print(vars.index('y',0,7)) # slice first then look for the perticular thing

