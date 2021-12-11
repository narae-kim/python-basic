# python -m pytest collection-level/namedtuple_example.py

from collections import namedtuple

task = namedtuple("Task", ["Summary", "Owner", "Done", "ID"])

# Set defaults for values that may not be provided
task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """
    Using no parameters should invoke the default values.
    """
    task_default = task()
    task_defined = task(None, None, False, None)
    assert task_default == task_defined


def test_member_access():
    """
    Test members of the task using dot notation.
    """
    t = task("New task", "Narae")  # other values will be defaults
    assert t.Summary == "New task"
    assert t.Owner == "Narae"
    assert (t.Done, t.ID) == (False, None)
