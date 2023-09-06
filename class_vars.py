# instance var made when we need to excitute a perticular property ina an object
# class vars are used for exituting ina pertiular class

class employee:
    company = 'google'  # assiociate to a class

    def __init__(self, name):
        self.name = name
        self.raisesalary = 2000  # will create an instance varable named raisesalary

    def showname(self):
        print(
            f'the name of the employee is {self.name} and the raise salary is {self.raisesalary} working in the company {self.company}')


emp1 = employee('ayush')
#  if i want to use increase raise salary
emp1.raisesalary = 3000  # can do definately
#  if i want to use another company name
emp1.company = 'Microsoft'  # this is a instance variable

#  for ayush it was microsoft ... but for pinki it still google  . why?
#  because there exist instance variable . else it takes class variable
emp1.showname()  # same
# employee.showname(emp1)  # same

emp2 = employee('pinki')
emp2.showname()  # same
