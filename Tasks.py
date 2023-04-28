# CLasses in Python
# A Class is like an object constructor or a blueprint for creating objects

# Example of Class

class PointBlank:                                   # This is how we define name of classes, we dont use underscore to define class
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

# Now we will define object

point1 = PointBlank()                               # Class our class as a function to define the object
point1.x = 20                                       # You can define attributes and can print them
point1.y = 30
print(point1.x, point1.y)                           # You can print with attaching function with attributes
point1.draw()                                       # You can call your defined methods execute

# We can create another object

point2 = PointBlank()
point2.x = 5                                        # We Need to define the attributes seperately for newly made object also
point2.y = 10
print(point2.x, point2.y)                           # You can call your defined methods to execute
point2.move()