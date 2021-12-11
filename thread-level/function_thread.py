# we can run threads concurrently - at the same time
# there is always a main thread, which can spawn additional threads
# additional threads then (re)join the main thread when done

from threading import Thread
import time
import random
import sys


def random_sleep_function(name):
    """
    A thread runnable function.
    """
    for i in range(1, 50):
        time.sleep(random.random() * 0.1)
        sys.stdout.write('{}\n'.format(name))


if __name__ == '__main__':
    thread1 = Thread(target=random_sleep_function, args=('thread1',))  # args must be a tuple
    thread2 = Thread(target=random_sleep_function, args=('thread2',))
    thread3 = Thread(target=random_sleep_function, args=('thread3',))
    thread4 = Thread(target=random_sleep_function, args=('thread4',))
    # start the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    # join to the main thread
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
