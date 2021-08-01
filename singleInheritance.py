class Apple:
    manufacturer = 'Apple'
    contact  = 'apple.com/contacts'
    
    
    # def __init__(self):
    #     self.location  = 'US'

    # def getLocation(self):
    #     return self.location

    def contactDetails(self):
        print('Hello, please log on to {}'.format(self.contact))
    
class MacBook(Apple):
    def __init__(self):
        self.yearOfRelease = 1990
        pass
    def manufacturerDetails(self):
        print('{0} manufactured MacBook in the year {1}'.format(self.manufacturer, self.yearOfRelease))
    

class Iphone(Apple):
    def  __init__(self):
        pass


macBook = MacBook()
macBook.manufacturerDetails()
macBook.contactDetails()


macBook.manufacturer = 'Microsoft'
print(macBook.manufacturer)
print(macBook.__dict__)

m2 = MacBook()
print(m2.manufacturer)

