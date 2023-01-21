# Define an exception named OutOfRangeError. Write a function named name_the_number that asks the user for an integer, and if it's equal to 1, prints "one"; if it's equal to 2, prints "two", and if it's equal to 3, prints "three". If the the parameter is not one of those three values, the function should raise an OutOfRangeError. Write code that calls name_the_number in a try block, and handles the possible OutOfRangeError in an except block. It should handle an OutOfRangeError by printing "That's not one of the allowed values!"

#define exception OutofRangeError
class OutOfRangeError(Exception):
    """someDescription
    """
#define name_the_number
def name_the_number():
    try:
        integer = int(input("please enter integer between 1 and 3")
        if integer > 3 or integer < 1:
            raise OutOfRangeError
        elif integer == 1: 
            print("one")
        elif integer === 2: 
            print("two")
        elif integer === 3: 
            print("three")

    except OutOfRangeError:
        print("Not allowed!")

name_the_number()

# In this example, I have defined an exception named OutOfRangeError and described the exception. Then I have defined a function name_the_number() that prompts the user to enter an integer, and if the entered integer is greater than 3 or less than 1, it raises an OutOfRangeError exception.
# if the integer is between 1 and 3 it checks if it's 1, 2 or 3 and prints the corresponding value.
# Then, I have called this function inside a try block and handled the possible OutOfRangeError in an except block. If the OutOfRangeError is raised, it will print the message "That's not one of the allowed values!"

# You can also specify the range of allowed values in the error message for the user to know.

# In Python, the **`try`**-**`except`** block is used to handle exceptions, or unexpected events, that may occur in a program. It allows you to test a block of code for errors, and handle those errors differently than the rest of the code.

# The basic structure of a try-except block is:

# ```
# Copy code
# try:
#     # code that may cause an exception
# except ExceptionType:
#     # code to handle the exception

# ```

# - The code that may cause an exception is placed inside the **`try`** block.
# - If an exception is raised, the code inside the **`except`** block will be executed.
# - The **`ExceptionType`** is the type of exception that you are trying to catch. If you don't specify an exception type, the **`except`** block will catch any exception.
# - If an exception occurs, the interpreter will immediately exit the try block and start executing the code in the except block. If an exception does not occur, the code in the except block will be skipped and the code after the except block will continue to execute.

# You can also use the **`finally`** block, which is executed regardless of whether an exception was raised or not.

# ```
# Copy code
# try:
#     # code that may cause an exception
# except ExceptionType:
#     # code to handle the exception
# finally:
#     # code that will always be executed

# ```

# **`try`**-**`except`** block allows you to handle errors gracefully, rather than crashing the program. It can also help to make your code more readable by separating the normal flow of control from the error handling code.