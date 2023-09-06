from ayu import impfile, ayu
from ayu import *
import ayu as a
from math import sqrt, pi  # importing a specific function
from math import *  # not always recommanded  # importing all
from math import sqrt as s  # importing a specific function
import math as m  # importing a moduile
import math
from pydoc import importfile  # importing a moduile
result = math.sqrt(9)
print(result)

result = m.sqrt(9)
print(result)

result = sqrt(9)*pi
print(result)

result = s(9)
print(result)

print(dir(m))

print(math.nan, type(math.nan))

#  impooting my own module
impfile()
print(ayu)

print(a.ayu)
