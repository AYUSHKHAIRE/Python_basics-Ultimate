class employee:
    def __init__(self, id, name):
        self.name = name
        self.id = id

    def showdetails(self):
        print(
            f'the name of the employee is {self.name} and the id is {self.id}')


class programmer(employee):
    def lang(self):
        print('the programmer uses python')


e = employee(32, 'rohan')
e.showdetails()

e2 = programmer(1200, 'ayush')
e2.showdetails()
e2.lang()
