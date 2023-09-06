m = {76, 56, 98, 44, 34, 43}

# for marks in m:
#     print(marks)
#     if(index == 2):
#         print("ayush , ausome !!")

# its linter - a syntex error

# to run code
index = 0
for marks in m:
    print(marks)
    if (index == 2):
        print("ayush , ausome !!")
    index += 1
print("\n")
# but declearing a variable can be frustating right ?

# method
for index, marks in enumerate(m):
    print(marks)
    if (index == 2):
        print("ayush , ausome !!")
        # as simple as that
print("\n")

#  as we know index starts from 0
#  you can justify starting point by passing an argument
for index, marks in enumerate(m, start=2):
    print(marks)
    if (index == 2):
        print("ayush , ausome !!")
        # as simple as that
