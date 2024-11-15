from enum import Enum
from shapes import (
    Square,
    Rectangle,
    Circle
)


SHAPES = ["Square", "Rectangle", "Circle"]


def shapes_program():

    user_input = input("Enter shape and parameters: ")
    user_input = user_input.split()
    user_shape = user_input[0].capitalize()
    numbers = []
    perimeter = 0
    area = 0

    if user_shape.capitalize() in SHAPES:
        for number in user_input:
            try:
                number = float(number)
                numbers.append(number)
            except ValueError:
                continue
    else:
        return "We don't have this shape"
        
    
    if user_shape == SHAPES[0] and len(numbers) == 3:
        shape = Square(numbers)
        if shape.side < 0:
            return "The side of a squere cannot be negative"    
    elif user_shape == SHAPES[1] and len(numbers) == 4:
        shape = Rectangle((numbers[0], numbers[1]), (numbers[2], numbers[3]))
    elif user_shape == SHAPES[2] and len(numbers) == 3:
        shape = Circle(numbers)
        if shape.radius < 0:
            return "The radius of a circle cannot be negative"

    else:
        return "Invalid number of parameters for the shape."
    perimeter = shape.perimeter()
    area = shape.area()
    
    return f"{user_shape} Perimeter {perimeter}, Area {area}"
        
