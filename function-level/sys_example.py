import sys  # access to the platform we are running upon

print(sys.version, sys.version_info)
print(sys.path)
print(sys.platform)
print(sys.base_prefix)

# we can pass in system arguments when we invoke a python module
# NB run this as follows:
# python function-level\sys_example.py arg1 arg2
# argv[0] is always the name of the module itself
# print(sys.argv[1], sys.argv[2])  # careful - sys.argv[0] is always the name of the module itself

# Reference counting
a = "A string"
print("Refcount: ", sys.getrefcount(a))  # the print and sys.getrefcount also increase the number
b = [a]
print("Refcount: ", sys.getrefcount(a))
c = {"key": a}
print("Refcount: ", sys.getrefcount(a))