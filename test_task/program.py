from enum import Enum
from test_task.shapes import (
    Square,
    Rectangle,
    Circle
)


SHAPES = ["Square", "Rectangle", "Circle"]


def shapes_program():

    user_input = input("Enter shape and parameters: ")
    user_input = user_input.split()
    shape = user_input[0].capitalize()
    numbers = []
    perimeter = 0
    area = 0

    if shape.capitalize() in SHAPES:
        for number in user_input:
            try:
                number = float(number)
                numbers.append(number)
            except ValueError:
                continue
    else:
        return "We don't have this shape"
        
    
    if shape == SHAPES[0] and len(numbers) == 3:
        square = Square((numbers[0], numbers[1]), numbers[2])
        if square.side < 0:
            return "The side of a squere cannot be negative"
        perimeter = square.perimeter()
        area = square.area()
    elif shape == SHAPES[1] and len(numbers) == 4:
        rectangle = Rectangle((numbers[0], numbers[1]), (numbers[2], numbers[3]))
        perimeter = rectangle.perimeter()
        area = rectangle.area()
    elif shape == SHAPES[2] and len(numbers) == 3:
        circle = Circle((numbers[0], numbers[1]), numbers[2])
        if circle.radius < 0:
            return "The radius of a circle cannot be negative"
        perimeter = circle.perimeter()
        area = circle.area()
    else:
        return "Invalid number of parameters for the shape."
    
    return f"{shape} Perimeter {perimeter}, Area {area}"
        
