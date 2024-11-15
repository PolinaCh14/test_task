from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, top_right,  bottom_left):
        self.top_right = top_right
        self.bottom_left = bottom_left

    def width_height(self):
        width = abs(self.top_right[0] - self.bottom_left[0])
        height = abs(self.top_right[1] - self.bottom_left[1])
        return width, height
    
    def perimeter(self):
        width, height = self.width_height()
        return 2 * (width + height)
    
    def area(self):
        width, height = self.width_height()
        return width * height

class Square(Rectangle):

    def __init__(self, top_right, side):
        super().__init__(top_right=top_right,
                         bottom_left =(top_right[0]-side , top_right[1]-side))
        self.side = side
        

    



class Circle(Shape):

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def perimeter(self):
        p = 2 * pi * self.radius
        return round(p, 2)
    
    def area(self):
        a = pi * self.radius ** 2
        return round(a, 2)