# Treating function as first class-citizens

# Below function returns another function
def getFunc(tag):

    def printTagLine(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    
    return printTagLine


loggerFunc_h1 = getFunc('h1')
loggerFunc_h1('Hello world1')

loggerFunc_p = getFunc('p')
loggerFunc_p('This is a sample paragraph')
