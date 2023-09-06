class person:
    # name = 'ayush'
    # salary = 1000
    # job = 'data scientist'

    def __init__(self, n, o):
        print("hey i am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(
            f"hey here my name is {self.name} , I am a {self.occ}")


a = person("ayush", "developer")

# a.name = 'chintui'
# a.salary = 1200
# a.job = 'programmer'

# print(f"the name is {a.name} and salary is {a.salary} $ ")

a.info()
