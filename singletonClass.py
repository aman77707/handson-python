"""
    Class Variable which will hold the singleton object
    We need static variable that is going to return the singleton object 
    If the singleton object was not created yet, it should create and return a new object
"""

class Singleton(object):
    __instance = None
    
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton("Default Name", 25)
        return Singleton.__instance

    def __init__(self, name, age):
        if Singleton.__instance is not None:
            raise Exception('Singleton instance was already created. It cannot be created more than once!')
        self.name = name
        self.age = age
        Singleton.__instance = self
    
# s0 = Singleton('Virat', 30)
# print(s0.__dict__)
# print(s1.__dict__)
obj = Singleton.getInstance()
print(obj.__dict__)
obj.name = 'Virat'
obj.age = 30
print(obj.__dict__)
# print(id(obj) == id(s0))

# s1 = Singleton('Aman', 30)