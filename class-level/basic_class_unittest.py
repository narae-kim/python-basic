import unittest

from basic_class import BasicClass


class TestBasicClass(unittest.TestCase):  # inherit from TestCase
    """
    The name of each test case has to start with "test".
    """

    def setUp(self):
        """
        Set up before each test runs.
        """
        self.basic_class = BasicClass(5)  # each test is independent

    def testCountInstances(self):
        """
        The number of BasicClass instances.
        The static variable is tricky to test.
        """
        self.assertGreaterEqual(BasicClass.count, 1)
        self.assertEqual(self.basic_class.count_instances(), "The BasicClass has 1 instances.")

    def testZCountInstances(self):
        """
        The number of BasicClass instances.
        The static variable is tricky to test.
        Since this test executed at last (name starting with "Z"), the number instances of BasicClass is 11 after running Setup() each time.
        """
        self.assertGreaterEqual(BasicClass.count, 1)
        self.assertEqual(BasicClass.count, 11)
        self.assertEqual(self.basic_class.count_instances(), "The BasicClass has 11 instances.")

    def testGetter(self):
        """
        The getter should return the value of the integer_instance_variable.
        """
        self.assertEqual(self.basic_class.integer_instance_variable, 5)

    def testStr(self):
        """
        The str should return the string of the integer_instance_variable.
        """
        self.assertEqual(str(self.basic_class), str(self.basic_class.integer_instance_variable))

    def testRepr(self):
        """
        The repr should return the debugging info.
        """
        self.assertEqual(repr(self.basic_class), "This class is has the integer instance variable of value {}.".format(
            self.basic_class.integer_instance_variable))

    def testSetterWithNegativeInt(self):
        """
        The setter only updates if the value is positive int.
        """
        self.basic_class.integer_instance_variable = -5
        self.assertEqual(self.basic_class.integer_instance_variable, 5)

    def testSetterWithPositiveInt(self):
        """
        The setter updates if the value is positive int.
        """
        self.basic_class.integer_instance_variable = 7
        self.assertEqual(self.basic_class.integer_instance_variable, 7)

    def testSetterWithZero(self):
        """
        The setter only updates if the value is positive int.
        """
        self.basic_class.integer_instance_variable = 0
        self.assertEqual(self.basic_class.integer_instance_variable, 5)

    def testSetterWithFloat(self):
        """
        The setter only updates if the value is positive int.
        """
        self.basic_class.integer_instance_variable = 7.0
        self.assertEqual(self.basic_class.integer_instance_variable, 5)

    def testSetterWithStr(self):
        """
        The setter only updates if the value is positive int.
        """
        self.basic_class.integer_instance_variable = "7"
        self.assertEqual(self.basic_class.integer_instance_variable, 5)

    def testIterator(self):
        """
        Test iter and next.
        """
        basic_class_iter = iter(self.basic_class)
        self.assertEqual(basic_class_iter.__next__(), 0)
        self.assertEqual(next(basic_class_iter), 1)
        self.assertEqual(basic_class_iter.__next__(), 2)
        self.assertEqual(next(basic_class_iter), 3)
        self.assertEqual(basic_class_iter.__next__(), 4)
        self.assertEqual(next(basic_class_iter), 5)
        with self.assertRaises(StopIteration):
            next(basic_class_iter)


if __name__ == '__main__':
    unittest.main()  # invoke the test cases
