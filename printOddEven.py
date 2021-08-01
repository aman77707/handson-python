import threading

import time

event_even = threading.Event()
event_odd = threading.Event()

def even_function():
    for i in range(0,11, 2):
        print(i)
        event_odd.set()
        event_even.clear()
        if i < 10: event_even.wait()

def odd_function():
    event_odd.wait()
    for i in range(1,10, 2):
        print(i)
        event_even.set()
        event_odd.clear()
        if i < 9: event_odd.wait()

t1 = threading.Thread(target=even_function)
t2 = threading.Thread(target=odd_function)

t1.start()
t2.start()

t1.join()
t2.join()
# print('END')