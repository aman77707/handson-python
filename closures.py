def outerFunction():

    message = 'Hello world'

    def innerFunction():
        print(message)
    
    return innerFunction

myFunction = outerFunction()
myFunction()