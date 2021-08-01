class car:
    # the variables defined here are the class properties
    wheels = 4


    def __init__(self):
        # variables defined here are the instance properties
        self.color = 'white'
        self.ac = -1
    
    # classmethods take the 1 positional argument by default
    @classmethod  # This type of method is equivalent to the C++ static methods
    def wheelNums(cls):
        print('This car has: ' + str(car.wheels) + ' wheels')

    @staticmethod
    def welcomeMessage():
        print('Hello, welcome to the car')
        car.wheels = 11
    

    def shiftGear(self):
        print('This is the shift gear in the car class: ' + str(car.wheels))
  
if __name__ == '__main__':
    
    c1 = car()
    print(car.wheels)
    if car.wheels == 4:
        print('The value is same as 4')
    print(c1.wheels)

    c2 = car()
    print(c2.wheels)
    c2.wheelNums()

    c2.wheels = 10
    print(c2.wheels)
    print(c1.wheels)
    print(car.wheels)
    c1.welcomeMessage()
    print(c1.__dict__)
    print(c2.__dict__)
    c1.shiftGear()
