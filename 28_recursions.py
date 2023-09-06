# exapme = factorial 
# 7! = 1x2x3x4x5x6x7
# 7!=7x6!
# 0!=1
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) #recursive approach
print(factorial(6))
print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))

