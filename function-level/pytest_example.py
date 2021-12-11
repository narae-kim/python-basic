# No need to import pytest
# pytest will look for functions whose name start with "test_"
# Invoke pytest like this: "python -m pytest pytest_example.py"


def test_tuple_pass():
    """
    The order in tuple matters. The test will pass with the same ordinal values.
    """
    assert (1, 2, 3) == (1, 2, 3)


def test_tuple_fail():
    """
    The order in tuple matters. The test will fail with different ordinal values.
    """
    assert (1, 2, 3) == (3, 2, 1)


def test_set_pass():
    """
    The order in set does NOT matter. The test will pass with different ordinal values.
    """
    assert {1, 2, 3} == {3, 2, 1}
