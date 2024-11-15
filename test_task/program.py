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
        
    try:
        if user_shape == SHAPES[0]:
            shape = Square(numbers)    
        elif user_shape == SHAPES[1]:
            shape = Rectangle(numbers)
        elif user_shape == SHAPES[2]:
            shape = Circle(numbers)
    except Exception as e:
        return str(e)

    
    perimeter = shape.perimeter()
    area = shape.area()
    
    return f"{user_shape} Perimeter {perimeter}, Area {area}"
        
