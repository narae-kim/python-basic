class BasicClass():
    """
    A class encapsulates features or some aspects of the reality.
    If no inheritance is given to the class as the empty bracket after the name of the class, then it is like BasicClass(object).
    All classes inherit from the Python Object class.
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
        if type(new_int) is int:
            self.__integer_instance_variable = new_int

    def count_instances(self):
        print("The BasicClass has {} instances.".format(self.count))

    def __str__(self):
        """
        This is similar to toString() in Java.
        """
        return "This class is has the integer instance variable of value {}.".format(self.__integer_instance_variable)


if __name__ == '__main__':
    b = BasicClass(1)
    print(b.__doc__)
    print(b.integer_instance_variable)
    b.integer_instance_variable = 2
    print(b.integer_instance_variable)
    b.__integer_instance_variable = 3  # create a brand new property!
    print("New property: ", b.__integer_instance_variable)
    print("Class property: ", b.integer_instance_variable)

    print(b)  # use __str__ function

    b1 = BasicClass(10)
    b2 = BasicClass(20)
    b.count_instances()
