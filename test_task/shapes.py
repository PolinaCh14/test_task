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

    def __init__(self, numbers):
        self.top_right = (numbers[0], numbers[1])
        self.bottom_left = (numbers[2], numbers[3])

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

    def __init__(self, numbers):
        self.side = numbers[2]
        super().__init__([numbers[0], numbers[1],numbers[0]-self.side , numbers[1]-self.side])
        
        


class Circle(Shape):

    def __init__(self, numbers):
        self.center = (numbers[0], numbers[1])
        self.radius = numbers[2]
    
    def perimeter(self):
        p = 2 * pi * self.radius
        return round(p, 2)
    
    def area(self):
        a = pi * self.radius ** 2
        return round(a, 2)