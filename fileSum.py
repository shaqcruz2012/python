def file_sum(file_name):
    try:
        with open(file_name) as f:
            numbers = [float(line.strip()) for line in f]
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    total = sum(numbers)
    with open("sum.txt", "w") as f:
        f.write(str(total))
# Write a function named file_sum that takes as a parameter the name of a text file that contains a list of numbers, one to a line, like this:

# 23.77
# 116
# 94
# -12.8
# 0
# 14.999

# The function should sum the values in the file and write the sum (just that number) to a text file named sum.txt. If the function can't find the file containing the list of numbers throw a FileNotFoundError.

##### Test Cases
import os

def test_file_sum():
    # Test with a valid file
    with open("test.txt", "w") as f:
        f.write("23.77\n116\n94\n-12.8\n0\n14.999")
    file_sum("test.txt")
    with open("sum.txt") as f:
        assert f.read() == "240.869"
    os.remove("test.txt")
    os.remove("sum.txt")

    # Test with non-existent file
    try:
        file_sum("non-existent.txt")
    except FileNotFoundError as e:
        assert str(e) == "File not found"

    # Test with empty file
    with open("test.txt", "w") as f:
        pass
    file_sum("test.txt")
    with open("sum.txt") as f:
        assert f.read() == "0.0"
    os.remove("test.txt")
    os.remove("sum.txt")
