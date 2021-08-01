"""
    1. class methods and static methods can also be inherited
    2. If a child class does't have an init method defined then upon it's instantiation parent's init method is invoked.
       If the number of arguments taken by the parens't init method doesn't match with the number of passed arguments when creating the child object,
       then it result in error(This is because the init method is inherited if not define in the child class, if define, it means init() is overridden).
    3. If a child has an init method defined then, init method of child is invoked. In this case to initialize the parent specific instance attributes, 
       child needs to call the parent's init method using the super() function or the parent class name.
    4. You can call the class methods using instances as well, but that is not the right way of accessing the class methods
    5. Class methods can also be used as an alternative constructors
"""



class Person:
    motto = "live and let live"
    
    def __init__(self, name):
        self.name = name
        print('Parent class init method')
    
    def displayName(self):
        print("Hello my name is {}".format(self.name))
    
    @classmethod
    def helloWorld(cls):
        print('This is class method of Persons')

    @staticmethod
    def dummyStaticMethod():
        print('This is parents static method')

class Student(Person):
    # def __init__(self, name):
    #     # self.id = 123
    #     # # super(Student, self).__init__(name)
    #     # Person.__init__(self, name)
    #     print('Child class init method')
    pass
        
    

s = Student('Aman')
# print(s.motto)
# print(s.name)
# print(s.id)
# print(s.__dict__)
s.helloWorld()
s.displayName()
s.dummyStaticMethod()
# s.displayName()

# p = Person('Virat Kohli')
# print(p.__dict__)
# print(p.motto)
# print(s.motto)
# Person.motto = 'Stay hungry stay foolish'
# print(p.motto)
# print(s.motto)
