from abc import ABC, abstractclassmethod

class Person(ABC):
    @abstractclassmethod
    def typeOfPerson(self):
        return 0

class Teacher(Person):
    def __init__(self):
        pass

    def typeOfPerson(self):
        print('This person is a teacher')

class Student(Person):
    def __init__(self):
        pass

    def typeOfPerson(self):
        print('This person is a student')

class FactoryClass:
    def buildObject(self, personType):
        if personType == 'Student':
            return Student()
        if personType == 'Teacher':
            return Teacher()

        # If another persont type is added in the library like below, then client doesn't have to change at all.
        # if personType == 'Staff':
        #     return Staff()
        raise Exception('Not a valid person type')

# Client code
class Client:
    def __init__(self):
        factory = FactoryClass()
        obj = factory.buildObject('Student')
        print(type(obj))

c = Client()

