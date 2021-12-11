import doctest


def range_square(*args):
    """
    doctest
    >>> range_square(2, 4)
    [4, 9, 16]
    >>> range_square(5)
    [1, 4, 9, 16, 25]
    >>> range_square(3.0)
    Traceback (most recent call last):
     ...
    TypeError: The input value has to be int type.
    """

    def filter_int(input):
        if type(input) is int:
            return input
        else:
            raise TypeError("The input value has to be int type.")

    if len(args) == 1:
        end = filter_int(args[0])
        start = 1
    elif len(args) == 2:
        start = filter_int(args[0])
        end = filter_int(args[1])
    result = []
    for i in range(start, end + 1):
        result.append(i * i)
    return result


if __name__ == '__main__':
    doctest.testmod(verbose=True)
