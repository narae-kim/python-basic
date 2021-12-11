from threading import Thread  # this is a thread access object
import time
import random


class RunnableClass(Thread):
    """
    A runnable class which descends from Thread class.
    """

    def __init__(self, name):
        Thread.__init__(self)  # call the super __init__
        self.name = name

    def run(self):
        """
        Override the run method of Thread.
        The run will be called every time we start a thread using this class.
        """
        for i in range(1, 50):
            time.sleep(random.random() * 0.1)
            print(self.name)


if __name__ == '__main__':
    t1 = RunnableClass('Class Thread 1')
    t2 = RunnableClass('Class Thread 2')
    t3 = RunnableClass('Class Thread 3')
    t4 = RunnableClass('Class Thread 4')
    # start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # join them
    t1.join()
    t2.join()
    t3.join()
    t4.join()
