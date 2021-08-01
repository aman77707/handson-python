class MusicalInstruments:
    numberOfMajorKeys = 12
    name = 'Abc'

class StringInstruments(MusicalInstruments):
    woodType = 'toneWood'
    name = 'xyz'

    def display(self):
        print('Hello world from StringInstruments')

class Guitar(StringInstruments):
    name = 'Aman'
    def __init__(self):
        self.numberOfStrings = 6
        print('This is Guitar, that has woodtype of {}, and number of major keys are {} also numberOfStrings are {}'.format(self.woodType, self.numberOfMajorKeys, self.numberOfStrings))
        print(self.name)
    
    def display(self):
        print('Hello world from Guitar')
    

g = Guitar()
print(g.__dict__)
g.display()