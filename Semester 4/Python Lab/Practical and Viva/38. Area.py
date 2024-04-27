import math
class Calculate:
    def area(self,**kwargs):
        if "radius"  in kwargs:
            return self.circle(**kwargs)
        elif "length" in kwargs and "breadth" in kwargs:
            return self.rectangle(**kwargs)
        elif "base" in kwargs and "height" in kwargs:
            return self.triangle(**kwargs)
        
    def circle(self,**kwargs):
        radius = kwargs["radius"]
        return math.pi*(radius**2)
    
    def rectangle(self, **kwargs):
        length = kwargs["length"]
        breadth = kwargs["breadth"]
        return length * breadth

    def triangle(self, **kwargs):
        base = kwargs["base"]
        height = kwargs["height"]
        return 0.5 * base * height

Calculate_obj = Calculate() 

circle_area = Calculate_obj.area(radius=5)
print("\nArea of circle:", circle_area)

triangle_area = Calculate_obj.area(base=3, height=4)
print("\nArea of triangle:", triangle_area)

rectangle_area = Calculate_obj.area(length=4, breadth=6)
print("\nArea of rectangle:", rectangle_area)