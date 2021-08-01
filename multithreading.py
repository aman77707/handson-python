import time, threading

globalVar = [10]

start = time.perf_counter()

def doSomething(seconds):
    localVar = ['Hello world']
    print(f'Sleeping for {seconds} second(s)..')
    time.sleep(seconds)

    # Global variable is going to be common for all the threads
    print('Done sleeping globalVar {}'.format(id(globalVar)))

    # Local variable is going to be created for every thread and hence will not be common to all the threads
    print('Done sleeping localVar {}'.format(id(localVar)))

threads = []
for i in range(10):
    t = threading.Thread(target=doSomething, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# t0 = threading.Thread(target=doSomething)
# t1 = threading.Thread(target=doSomething)

# t0.start()
# t1.start()

# t0.join()
# t1.join()

finish = time.perf_counter()

print('Total time taken: {}'.format(round(finish - start,2)))


# Without threading
# start = time.perf_counter()

# def doSomething():
#     print('Sleeping for one second..')
#     time.sleep(1)
#     print('Done sleeping for one second..')

# doSomething()
# doSomething()


# finish = time.perf_counter()

# print('Total time taken: {}'.format(round(finish - start)))