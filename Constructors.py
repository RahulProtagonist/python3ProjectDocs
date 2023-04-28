# Constructors in Python
# Constructors are generally used for istantiating an object
# Constructors is to initialize values to the data members of the class when an object of the class is created.
# _init_() method is called the constructors and is always called when an object is created

# Syntax of constructor

# def __init__(self)                        # Self is the reference to the current object
    # Body of the constructor

# There are two types of constructors
# Default Constructor
# The default constructor is a simple constructor which does not accept any arguments
# Its definition has only one argument which is a reference to the instance being constructed

# Parameterized Constructor
# It is a constructor with parameters
# The parameterized constructor takes its first argument as a reference to the instance being constructed known as self
# and the rest of the arguments are provided


# Syntax example of constructor

#  class Point:
#   # def __init__(self, x, y):                     # This is how you define a Constructor
    # self.x = x
    # self.y = y


# Example of Constructor
# Car Name Start and Move Turn and come back

class SigmaFour:                                    # SigmaFour is the class name
    def __init__(self, car):                         # Car is the constructor
        self.car = car

    def start(self):
        print(f'{self.car}', "has started")         # Car Start Method

    def move(self):
        print(f'{self.car}', "has moved")          # Car Moved Method

    def turn(self):
        print(f'{self.car}', "has turned")         # Car Turned Method

    def back(self):
        print(f'{self.car}', "has returned")       # Car Returned Method


vehicle = SigmaFour("Verna SX(O) A/T Crdi")                                # Attribute for the methods (Positonal Arguments
vehicle.start()
vehicle.move()
vehicle.turn()
vehicle.back()

