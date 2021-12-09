from abstract_class import AbstractClass


class ConcreteClass(AbstractClass):
    """
    Concrete class.
    """
    def __init__(self, string_instance_variable):
        """
        This method is similar to the constructor in Java, but it has more to that.
        """
        self.string_instance_variable = string_instance_variable  # calling the setter

    @property
    def string_instance_variable(self):
        """
        Before using setter, the name has to be defined first as a property.
        """
        return self.__string_instance_variable

    @string_instance_variable.setter
    def string_instance_variable(self, new_string):
        if type(new_string) is str and new_string != "":
            self.__string_instance_variable = new_string
        else:
            self.__string_instance_variable = "default"  # or raise an exception

    def abstract_method(self):
        #return super().abstract_method()
        print("Now this abstract method is overriden in the {}'s concrete class.".format(self.string_instance_variable))

    def some_method(self):
        #return super().some_method()
        print("I override this method :p")


if __name__ == '__main__':
    c = ConcreteClass("Narae")
    c.abstract_method()
    c.some_method()
    print(c.string_instance_variable)