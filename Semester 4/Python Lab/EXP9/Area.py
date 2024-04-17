"""Write a Python program to declare a class Calculate which calculates the Area of Circle,
Triangle and Rectangle (Use Method Overloading)."""


class Calculate:
  def area(self, **kwargs):
    if "radius" in kwargs:
      return self.area_circle(**kwargs)

    elif "length" in kwargs and "breadth" in kwargs:  
      return self.area_rectangle(**kwargs)

    elif "base" in kwargs and "height" in kwargs:
      return self.area_triangle(**kwargs)

    else:
      return "Invalid arguments"

  def area_circle(self, **kwargs):
    radius = kwargs["radius"]
    return 3.14 * radius * radius

  def area_rectangle(self, **kwargs):
    length = kwargs["length"]
    breadth = kwargs["breadth"]
    return length * breadth

  def area_triangle(self, **kwargs):
    base = kwargs["base"]
    height = kwargs["height"]
    return 0.5 * base * height

calculator = Calculate()
        
circle_area = calculator.area(radius=5)
print("\nArea of circle:", circle_area)

triangle_area = calculator.area(base=3, height=4)
print("\nArea of triangle:", triangle_area)

rectangle_area = calculator.area(length=4, breadth=6)
print("\nArea of rectangle:", rectangle_area)


