class OperatingSystem:
    multitasking = True
    name = 'MacOs'

class Apple:
    website = 'www.apple.com'
    name = 'Apple Inc.'

class MacBook(OperatingSystem, Apple):
    def __init__(self):
        self.year = 2020
        if self.multitasking:
            print('{} has manufactured Macbook in the year {}.'.format(self.website, self.year))
            # self.name is the common attribute in both the parent classes
            # Hence, it's value depends on the order of the inheritance of the base classes
            # Since we are inheriting OperatingSystem base class first so the value will be MacOs
            print(self.name)

mb = MacBook()
