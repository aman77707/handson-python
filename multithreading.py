import time

start = time.perf_counter()

def doSomething():
    print('Sleeping for one second..')
    time.sleep(1)
    print('Done sleeping for one second..')

doSomething()
doSomething()


finish = time.perf_counter()

print('Total time taken: {}'.format(round(finish - start)))