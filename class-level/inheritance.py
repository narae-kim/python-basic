# Python built-in stuffs - many of them are intrinsic to Python


class TopLevel():
    def __init__(self):
        pass


class Derived(TopLevel):
    """
    This class is derived from the TopLevel class.
    The modern approach is to use only ONE base class.
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Derived class instance"


if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(d)

    # The intrinsic members of the instances
    print("\n\nClass name is {}".format(Derived.__name__))
    print("Class docstring is {}".format(Derived.__doc__))
    print("Class dictionary is {}".format(Derived.__dict__))
    print("Class bases are {}".format(Derived.__bases__))
