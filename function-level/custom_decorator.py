# decorator: starting with @ sign

def show_args(function):
    """
    A customised decorator function
    """
    def inner_function(*args, **kwargs):
        """
        *args: the tuple of all positional arguments
        **kwargs: the dict of all keyword arguments
        """
        print("We are running the function called '{}'.".format(function.__name__))
        print("Positional arguments are: {}".format(args))
        print("Keyword arguments are: {}".format(kwargs))
        return function(*args, **kwargs)
    return inner_function

# A normal function
@show_args
def add(x, y):
    return x + y


if __name__ == '__main__':
    x, y = (1, 2)  # common practice - unpack the tuple
    print(add(x, y))
    print(add(y=3, x=4))
