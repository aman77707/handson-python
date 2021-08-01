class Employee:
    def __init__(self, name):
        self.name = name
        print('This is the Employee class Init method')

class Trainee(Employee):
    def __init__(self, name):
        print('This the Trainee class Init method')
        self.id = 123
        super(Trainee, self).__init__(name)


t = Trainee('Aman')
print(t.__dict__)