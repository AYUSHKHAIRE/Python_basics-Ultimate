# with open('myfile2.txt', 'r') as f:
#     # f.write("hey i am inside with")
#     f.seek(10)
#     data = f.read(5)
#     print(data)
#     print(f.tell())

with open('sample.txt', 'w') as f:
    f.write('Hello World3!')
    f.truncate(3)  # write only 3 charactors

with open('sample.txt', 'r') as f:
    print(f.read())
