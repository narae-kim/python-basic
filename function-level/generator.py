import os

# Generators can yield values on demand.
r = range(10)

generator = (i for i in r)  # good for saving memory
list_generator = [i for i in r]  # good for computation but not memory - all the values exist in memory
generator_10 = (i for i in range(0, 101, 10))


def byte_generator(start, stop):
    n = start
    while n < stop:
        yield bytes(n)  # the 'yield' statement makes it into a generator - similar to 'return' but continues
        n += 1


def bad_file_read(filename):
    file = open(filename)
    lines = file.read().split("\n")  # split() adds each line in a list > possibly MemoryError
    return lines


def file_line_generator(filename):
    for row in open(filename, "r"):
        yield row  # lazy iterator - no MemoryError


def file_line_by_generator_comprehension(filename):
    __generator = (row for row in open(filename))
    return __generator


if __name__ == '__main__':
    print(r)
    print(generator)
    print(list_generator)

    print("-- Generator --")
    for item in generator:
        print(item, end=", ")

    print("\n-- List generator --")
    for item in list_generator:
        print(item, end=" - ")

    print("\n-- Generator try again --")
    # We cannot iterate over the generator again since it has been exhausted.
    for item in generator:
        print(item, end=", ")  # no output

    print("\n-- New generator --")
    print(generator_10.__next__())
    print(next(generator_10))
    print(generator_10.__next__())
    print(next(generator_10))

    print("\n-- Byte generator --")
    bg = byte_generator(10, 20)
    print(bg.__next__())
    for b in bg:
        print(b)

    print("\n-- File line generator --")
    sample_file_name = os.path.join("..", "resources", "Sample-Spreadsheet-5000-rows.csv")
    print(len(bad_file_read(sample_file_name)))
    sample_file_generator = file_line_generator(sample_file_name)
    print(next(sample_file_generator))
    sample_file_generator_comprehension = file_line_by_generator_comprehension(sample_file_name)
    print(next(sample_file_generator_comprehension))
