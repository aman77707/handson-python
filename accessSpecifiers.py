"""
    Convention:
        Public : memberName, Can be accessed by family of classes and the outside world
        Protected: _memberName, Should only be accessed by the family of classes
        Private: __memberName, Should only be accessed by the class in which it is present and not even in the family of the classes(derived classes)


        Name mangling is done for the private members of a class
"""



class Person:
    name = 'Aman'
    _age = 30
    __maritalStatus = 'Engaged'

    def dummyMethod(self):
        print('Hello')

    def __privateDummyMethod(self): # This is a private method
        print('This is a dummy private method')
    
    @classmethod
    def dummyMethodClass(cls):
        print('Hello from class method')

class AMAN(Person):
    def __init__(self):
        print(self._Person__maritalStatus) # Don't access private mebers of base class using name mangling hacks
        print(self.name)
        print(self._age) # This is fine


p = Person()
a = AMAN()
# print(a.__dict__)
# print(p.__dict__)
# print(Person.__dict__)
# print(p._Person__maritalStatus)
# print(Person._Person__maritalStatus)

p._Person__privateDummyMethod()