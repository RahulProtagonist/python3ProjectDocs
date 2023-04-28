# Modules in Python
# Modules contains deifinitions and statements for python
# A module can define functions, classes and variables
# Modules also include runnable code

# Example of Modules of Python

import calculatorModule                                 # We are importing calculatorModule
from calculatorModule import add

x = int(input("Enter First Number - "))
y = int(input("Enter Second Number - "))

aanswer = add(x, y)
print(aanswer)
