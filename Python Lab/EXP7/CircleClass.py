"""Write a Python class named Circle constructed by a radius and two methods which
will compute the area and the perimeter of a circle."""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def display(self):
        print("\nCircle Details:")
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


radius = int(input("\nEnter the radius of the circle:"))
Circle_obj = Circle(radius)
Circle_obj.display()