a = "ayush!! ayush!! ayush!" 
print(len(a))
# string are immutable
print(a.upper())
print(a.lower()) # this will not convert in lowercase as already in .
print(a.rstrip("!"))
print(a.replace("ayush","sdfg"))
print(a.split("  ")) #convert into list
name = "ayush"
name2 = "EEEayush"
print(name.capitalize())
print(name2.capitalize())
print(a.center(50))
print(len(a.center(50)))
print(a.count("ayus"))
a1 = "aaaaaaaaa"
print(a1.count("a"))
print(a1.endswith('aaa'))
a2 = "asdfg sdfg dfg fg g"
# #         ^   ^^
print(a2.endswith('fg',4,10))
print(a2.startswith('g',4,10))
print(a.find("us")) # returns that index number .,  Iff not present then returns -1
print(a.index("us")) # returns that index number .,  Iff not present then returns ERROR
a3 = "asd3232030203aaaa"
a4 = "asdaaaa"
print(a3.isalnum()) # looks for capitals smalls and numbers
print(a4.isalpha()) # looks for capitals smalls but not numbers
print(a4.islower()) # looks for smalls only
a5="asdedd s / dd//d/d"
a6="asdedd s / dd//d/d  \n"
a7="      " #spaces
a8="        " #tabs
print(a5.isprintable())
print(a6.isprintable())
print(a5.isspace())
print(a7.isspace())
print(a8.isspace())
a9 = "Ayu Raj Khs"
print(a9.istitle())
print(a.swapcase())
a10 = "asd cd vbf vb dfe d de"
print(a10.title())

if "ayu" in "ayush":
    print('yes')