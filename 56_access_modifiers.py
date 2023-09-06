#  public private protected
#  all vars are public by default
class employee:
    def __init__(self, id, name):
        self.name = 'ayush'
        self.__name = 'ayush'  # i cant access this


a = employee()
print(a.name)
# print(a.__name)
print(a._employee__name)  # indirect
print(a.__dir__)
