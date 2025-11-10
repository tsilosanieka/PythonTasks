# Import the math module for the value of Pi
import math

#Base Class
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return None


#Create Subclasses

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


#Polymorphism

def print_area(shape):
    print(f"Shape: {shape.name}, Area: {shape.area():.2f}")

# Create instances of the subclasses
my_rectangle = Rectangle(name="Large Rectangle", width=17, height=9)
my_circle = Circle(name="Small Circle", radius=6)

# Call the polymorphic function with different but related objects
print_area(my_rectangle)  # Calls Rectangle.area()
print_area(my_circle)  # Calls Circle.area()