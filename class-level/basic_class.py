import doctest


class BasicClass():
    """
    A class encapsulates features or some aspects of the reality.
    If no inheritance is given to the class as the empty bracket after the name of the class, then it is like BasicClass(object).
    All classes inherit from the Python Object class.
    This class implements some of Python built-in intrinsic operations.
    """
    # static variable (a property assigned to the class rather than instances)
    count = 0

    def __init__(self, integer_instance_variable):
        """
        This function is similar to a constructor in Java.
        """
        # property-name mangling (double underscore) - recommended
        self.__integer_instance_variable = integer_instance_variable
        # self.integer_instance_varaible = integer_instance_varible  # direct mutable object
        BasicClass.count += 1

    @property
    def integer_instance_variable(self):
        """
        Before using setter, the name has to be defined first as a property.
        This function is then a getter - read only.
        """
        return self.__integer_instance_variable

    @integer_instance_variable.setter
    def integer_instance_variable(self, new_int):
        """
        This function is a setter.
        The main purpose of setters is to sanitize the type and/or the value before assigning them.
        """
        if type(new_int) is int and new_int > 0:
            self.__integer_instance_variable = new_int

    def count_instances(self):
        """
        Return the number of instances of BasicClass.

        Quick doctest
        >>> basic_class.count_instances()
        'The BasicClass has 1 instances.'
        """
        return "The BasicClass has {} instances.".format(self.count)

    def __str__(self):
        """
        This is similar to toString() in Java.

        Quick doctest
        >>> str(basic_class)
        '5'
        >>> basic_class.__str__()
        '5'
        """
        return str(self.__integer_instance_variable)

    def __repr__(self):
        """
        This is debugging purpose. Showing the information about the object.

        Quick doctest
        >>> repr(basic_class)
        'This class is has the integer instance variable of value 5.'
        >>> basic_class.__repr__()
        'This class is has the integer instance variable of value 5.'
        """
        return "This class is has the integer instance variable of value {}.".format(self.__integer_instance_variable)

    def __iter__(self):
        """
        Make the class iterable.
        Here the iterator generates positive integer numbers from 0 to its number.
        """
        self.__iter_next = -1
        return self

    def __next__(self):
        if self.__iter_next < self.integer_instance_variable:
            self.__iter_next += 1
            return self.__iter_next
        else:
            raise StopIteration


if __name__ == '__main__':
    # doctest
    print("----- doctest ------")
    doctest.testmod(extraglobs={'basic_class': BasicClass(5)}, verbose=True)
    print("--------------------")

    b = BasicClass(1)
    print(b.__doc__)
    print(b.integer_instance_variable)
    b.integer_instance_variable = 2
    print(b.integer_instance_variable)
    b.__integer_instance_variable = 3  # create a brand new property!
    print("New property: ", b.__integer_instance_variable)
    print("Class property: ", b.integer_instance_variable)

    print(b)  # use __str__ function
    print(repr(b))

    b1 = BasicClass(10)
    b2 = BasicClass(20)
    print(b.count_instances())

    print("\n--- Iterator ---")
    b_iter = iter(b)
    for n in b_iter:
        print(n)

    b_iter2 = iter(b)
    print(b_iter2.__next__())
    print(next(b_iter2))
    b.integer_instance_variable = 5
    print(b_iter2.__next__())
    print(next(b_iter2))
    print(b_iter2.__next__())
    print(next(b_iter2))
