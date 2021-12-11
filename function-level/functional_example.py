# Functional programming has returned a pure function without side-effects, i.e. outputs are entirely predictable by given inputs.
from functools import reduce
import time
# from timeit import default_timer


def square(x):
    return x * x


def add(x, y):
    return x + y


def isodd(n):
    return n % 2 != 0  # True or False if even or odd


# cProfile is a performant way to profile non-trivial code
# python -m cProfile -o profiling_output functional_example.py
# number of calls, total times time per call, cumulative times
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # self-referencing


def fibonacci_by_reduce(n):
    seq = (1, 1)
    for _ in range(2, n + 1):
        seq += (reduce(lambda a, b: a + b, seq[-2:]),)  # e.g. (1,1,2,3,5,7,13,20,33,)
    return seq[n]


if __name__ == '__main__':
    # using 'map' the values into the function
    sq_l = list(map(square, range(1, 6)))
    print(sq_l)

    # using 'filter' function
    odd_l = list(filter(isodd, range(1, 10)))
    print(odd_l)

    # using 'reduce'
    r = reduce(add, odd_l, 10)  # sum every value from the odd list and add ten
    print(r)

    print("\n--- Fibonacci ---")
    start = time.time()
    # start = default_timer()  # much more platform independent
    print(fibonacci_by_reduce(40))  # fibonacci_by_reduce takes a fraction of a millisecond, fibonacci takes nearly a minute
    end = time.time()
    # end = default_timer()
    print("Fibonacci took {} seconds".format(end - start))
    start = time.time()
    print(fibonacci(40))  # cProfile will tell us the performance of this method
    end = time.time()
    print("Fibonacci took {} seconds".format(end - start))
