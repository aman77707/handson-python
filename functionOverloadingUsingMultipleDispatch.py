# class Sample:
#     def funct(self,a, b):
#         print('This is from first funct', a, b)

#     def funct(self,a):
#         print('This is from second funct', a)

# s = Sample()
# s.funct(10)
# s.funct(10, 11)

from multipledispatch import dispatch
  
#passing one parameter
@dispatch(int,int)
def product(first: int,second: int) -> None:
    result = first*second
    print(result);
  
#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result  = first * second * third
    print(result);
  
#you can also pass data type of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result  = first * second * third
    print(result);
  
  
#calling product method with 2 arguments
product(2,3,2) #this will give output of 12
product(2,3)
product(2.2,3.4,2.3) # this will give output of 17.985999999999997