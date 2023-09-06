# def double(x):
#     return x*2

# instad of this we can write

def double(x): return x*2  # like a shortform
def cube(x): return x*x*x
def avg(x, y): return (x+y)/2


print(double(5))
print(cube(5))
print(avg(5, 4))


def appl(fx, value):
    return 6 + fx(value)  # passing a function to a function


print(appl(cube, 2))
