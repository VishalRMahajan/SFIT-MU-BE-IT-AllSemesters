import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

    def circumference(self):
        return 2*math.pi*self.radius

    def display(self):
        print("\nCircle Details:")
        print("Radius:", self.radius)
        print("Area:", self.area())
        print("Perimeter:", self.circumference())

radius = int(input("Enter the Radius: "))
Circle_obj = Circle(radius)
Circle_obj.display()