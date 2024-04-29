## Functions

# The example custom functions used in the video are listed below:
# This function uses no parameters as input and can be simply
# called by it's name, say_hello()
def say_hello():
    print('Hello World!')

# This function uses 2 parameters to perform the add operation
# within it, therefore two numbers (strings will work too) will need
# to be provided as arguments when the function is called
# add_two_nums(4, 5)
def add_two_nums(num_1, num_2):
    print(num_1 + num_2)

# Instead of printing out the summed value of the two numbers, the
# function can be made to return the value instead. If nothing is
# specified by the explicit use of the return keyword, then the None
# datatype is returned by default by all functions to the caller
def add_two_nums(num_1, num_2):
    return num_1 + num_2

my_added_num = add_two_nums(4,5) # The return value from function
                                # call is being assigned to my_added_num
print(my_added_num)             # printing out value of my_added_num
# We can do this without the variable
print(add_two_nums(4,5))

# If we try to print out the value of a function call that returns None
# meaning no return value was specified, then it prints None to the screen
print(say_hello())
# The call above will return in Hello World being printed to the screen
# due to the code inside the function, followed by None, printed due
# to the print function printing the returned value from the function

# You can use doctstrings to provide information about your function
# Example docstring
def say_hello():
    """This function prints Hello World! to the screen"""
    print('Hello World!')

# More detailed docstring
def add_two_nums(num_1, num_2):
    """
    This function adds two objects
    Input: Two objects to add, num_1 and num_2
    Output: The value of the two objects added together
    """
    return num_1 + num_2

# In Python when a function returns multiple values separated by
# commas in its return statement, these values are returned as tuples
# which can then be unpacked by the caller
