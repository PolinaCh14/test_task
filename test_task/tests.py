from shapes import (
    Square,
    Rectangle,
    Circle
)


import unittest
from unittest import mock
from program import shapes_program 

class TestShapes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.square1_ = Square((1,1), 1)
        cls.square2_ = Square((2,2), 4)

        cls.rectangle1_ = Rectangle((2,2), (1,1))

        cls.circle1_ = Circle((1,1), 2)
    
    def test_correct_square_perimeter(self):

        perimeter_1 = self.square1_.perimeter()
        perimeter_2 = self.square2_.perimeter()

        self.assertEqual(perimeter_1, 4.0)
        self.assertEqual(perimeter_2, 16.0)
    
    def test_correct_square_area(self):
        area_1 = self.square1_.area()  
        area_2 = self.square2_.area()

        self.assertEqual(area_1, 1.0)  
        self.assertEqual(area_2, 16.0) 

    def test_correct_rectangle_perimeter(self):
        perimeter = self.rectangle1_.perimeter() 

        self.assertEqual(perimeter, 4.0)

    def test_correct_rectangle_area(self):
        area = self.rectangle1_.area()  

        self.assertEqual(area, 1.0)

    def test_correct_circle_perimeter(self):
        perimeter = self.circle1_.perimeter() 

        self.assertAlmostEqual(perimeter, 12.57, places=2)

    def test_correct_circle_area(self):
        area = self.circle1_.area()  

        self.assertAlmostEqual(area, 12.57, places=2)



class TestShapesProgram(unittest.TestCase):

    @mock.patch('builtins.input', return_value="Square TopRight 1 1 Side 2")
    def test_square(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "Square Perimeter 8.0, Area 4.0")
     
    @mock.patch('builtins.input', return_value="Rectangle TopRight 1 1 BottomLeft 3 3")
    def test_rectangle(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "Rectangle Perimeter 8.0, Area 4.0")

    @mock.patch('builtins.input', return_value="Circle Center 0 0 Radius 5")
    def test_circle(self, mock_input):
        result = shapes_program()
        self.assertAlmostEqual(result, "Circle Perimeter 31.42, Area 78.54", places=2)

    @mock.patch('builtins.input', return_value="Square TopRight 1 1 Side -1")
    def test_square_negative_side(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "The side of a squere cannot be negative")

    @mock.patch('builtins.input', return_value="Rectangle TopRight 1 1 BottomLeft 5")
    def test_invalid_rectangle_input(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "Invalid number of parameters for the shape.")

    @mock.patch('builtins.input', return_value="Circle Center 0 0 Radius -5")
    def test_circle_negative_radius(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "The radius of a circle cannot be negative")

    @mock.patch('builtins.input', return_value="Circle2ee Center 0 0 Radius -5")
    def test_invalid_shape(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "We don't have this shape")

    @mock.patch('builtins.input', return_value="Square TopRight 1 1")
    def test_invalid_square_input(self, mock_input):
        result = shapes_program()
        self.assertEqual(result, "Invalid number of parameters for the shape.")
    