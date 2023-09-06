class person:
    name = 'ayush'
    salary = 1000
    job = 'data scientist'

    def info(self):
        print(
            f"hey here my name is {self.name} , I am a {self.job} and my salary is {self.salary } $")


a = person()
a.name = 'chintui'
a.salary = 1200
a.job = 'programmer'

b = person()
b.name = 'pintui'
b.salary = 120099
b.job = 'hacker'
 
print(f"the name is {a.name} and salary is {a.salary} $ ")
print(f"the name is {b.name} and salary is {b.salary} $ ")
a.info()
b.info()
