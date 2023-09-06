# A setter updates the value of a variable, while a getter reads the value of a variable

class myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f'the value is {self._value}')

    @property  # work as a setter as it sets a value
    def ten_value(self):
        return 10*self._value
    # it seens like it is a property but in fact it is a method as it is hidden

    @ten_value.setter
    def ten_value(self, new):
        self._value = new/10


# obj.ten_value=56 cant change value as i got error
obj = myclass(10)
obj.ten_value = 45
# i want to access this then it should give 10x line(10) then i can apply property linev (8)
print(obj.ten_value)
obj.show()
