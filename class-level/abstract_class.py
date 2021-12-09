# Abstract Base Class to use inheritance
from abc import ABCMeta, abstractmethod, abstractproperty


class AbstractClass():
    """
    Abstract base (top-level) class.
    """
    __metaclass__ = ABCMeta  # now abc class can be subclassed

    @abstractmethod
    def abstract_method(self):
        pass  # no body

    @property
    @abstractmethod
    def string_instance_variable(self):
        pass

    def some_method(self):
        print("This method is defined from AbstractClass!")


if __name__ == '__main__':
    a = AbstractClass()
    a.some_method()
    print(a.string_instance_variable)
    print(a.__doc__)
