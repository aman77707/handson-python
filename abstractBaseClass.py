from abc import ABC, abstractclassmethod, abstractstaticmethod

class Base(ABC):
    @abstractclassmethod
    def area(self):
        return 0

class Child(Base):
    def __init__(self, name):
        self.name = name
        print('Name of the shape is {}'.format(self.name))
    
    def area(self):
        print('This is the area of the child class')

c = Child('Triangle')
c.area()

b = Base() # This will result in the run time error, because a class with an abstractclassmethod cannot be instantiated
