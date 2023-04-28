# Tuples in Python
# Tuples are like lists, but they cannot be modified
# Since lists are defined by '[]' , tuples are defined by '()'
# Items in tuples can also be accessed just like lists with 'Square Brackets'
# Example
# numbers = (1, 2, 3)
# print(numbers[10])

# Unpacking in Python
# Unpacking stores values so that it can use elsewhere easily with less amount of code
# Example

# coordinates - (1, 4, 7)
# x, y, z = coordinates         # Here values of coordinates are stored in x,y and z so if we want to pick the values in coordinates
                                # we just need to pick x,y,z
# print('Coordinates are ' f"{x}, {y}, {z}")

# Unpacking can also be used with lists and tuples

# Dictionaries in python
# In Dictionaries we store information which comes in key value pairs
# Example
# Name: Rahul       # Name is key, rahul is value
# Email: rahul@email.com    # Email is key, email id is value

# How to define a dictionary in python

# customer = {
#     "name": "Rahul Chandra" ,                   # Assign keys and their values in this format
#    "Location": "Rajasthan",
#     "is_legit": True                            # You can also add a boolean in the dictionary
# }
# customer["name"] = "Nunu Chandra"                 # This is how we can update the value in the key / same to add new key and it's value
# print(customer["name"])                         # To Print a key and it's value wirte the dictionary name and the key which you need

# .get method does'nt throw an error when a key is not found
# example - print(customer.get("Place"))

# Functions in Python
# It is a container that for a few lines of codes that perform a specific task
# Syntax for function - 'def' it stands for define, whenever 'def' is used interpreter will understand that we are defining a function
# By Default Function will return a 'None' Value
# Example for funtions

# Greeting Hello Function

# def namaste_function():             # Function Name
#     print("Hey There")
#     print("Hi There")               # Function Block
#    print("Namaste Dude")

                                    # Need to give two line breaks (Recommended)
# namaste_function()                  # Call this function and it will print you the data in it as output

# Parameters in python
# A parameter is the variable listed inside the parenthesis in the function definition
# example of Parameter

# def Hello_basic(param1, param2):
#     print(f'Hi {param1} {param2}')

# Hello_basic("Rahul", "Chandra")         # fill the values which needs to be passed in those two parameters


# Keyword Arguments
# Values that, when passed into a function, are identifiable by a specific parameter names.
# keyword argument is preceded by a parameter and the assignment operator, =. Keyword arguments can be likened to dictionaries in that they map a value to keyword
# Keyword arguments are mostly used for numerical values reccomended to use positional arguments for characters

# Return Statement
# this is used to return the result to whoever using the function
# this is used in complex calculations

# Example
# def square(number):
#       return number * number                      # Add return to get tne calculation of this statement

# result = square(3)
# print(result)

# Creating a reusable function
# Refer Emoji Converter Program

# Exceptions in Python
# An Exception is an event, which ovvurs during the execution of a program that disrupts the normal flow of the program's instructions.
# In General, when a python script encounters a sitaution that it cannot cope with,it raises an exception
# An Exception is a python object that represents an error

# Example

# try:
#     age = input(('Age: '))                              # with 'try' the code wont be end abruptly
#     income = 25000
#     risk = income / age
#     print('Printed age is ' f'{age}')
#     print('Risk is ' f'{risk}')
# except ZeroDivisionError:                               # 'ZeroDivisionError' is a type which comes if you enter zero in value in a division operation
#     print("Age cannot be zero!!!")
# except ValueError:
#     print("Wrong value!!!")
