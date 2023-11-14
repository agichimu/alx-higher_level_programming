#!/usr/bin/python3
""" Rectangle test module """
import unittest
import sys
import pep8
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class Rectangle_test(unittest.TestCase):
    """ Rectangle Test """

    def test_pep8(self):
        """ pep8 test """
        pep8style = pep8.StyleGuide(quiet=True)
        output = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(output.total_errors, 0)

    def test__init__normally(self):
        """ Constructor test normal conditions """
        r = Rectangle(3, 6, 0, 0, 1)
        self.assertTrue(r.id == 1)  # inheritance from Base
        self.assertTrue(r.width == 3)
        self.assertTrue(r.height == 6)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)

    def test__init__arguments_position(self):
        """ Constructor test argument positions """
        with self.assertRaises(TypeError) as error:
            Rectangle()  # zero arguments
        self.assertTrue(str(error.exception) == "\
__init__() missing 2 required positional arguments: 'width' and 'height'")
        with self.assertRaises(TypeError) as error:
            Rectangle(1)  # one paramter
        self.assertTrue(str(error.exception) == "\
__init__() missing 1 required positional argument: 'height'")
        r = Rectangle(1, 1)  # Two paramenters: width and height
        self.assertTrue(r.width == 1)
        self.assertTrue(r.height == 1)
        r = Rectangle(1, 1, 1)  # three paramenters: width, height and x
        self.assertTrue(r.x == 1)
        r = Rectangle(1, 1, 1, 1)  # three paramenters: width, height and y
        self.assertTrue(r.y == 1)

    def test__init__no_allowed_values(self):
        """ Constructor negative numbers and zero """
        with self.assertRaises(TypeError) as error:
            Rectangle("string", 0)  # string width"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(10, "string")  # string height"
        self.assertTrue(str(error.exception) == "height must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle([1], 0)  # list width"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(10, [1])  # list height"
        self.assertTrue(str(error.exception) == "height must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(0.0, 0)  # float width"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(10, 0.0)  # float height"
        self.assertTrue(str(error.exception) == "height must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle((2,), 0.0)  # tuple widht"
        self.assertTrue(str(error.exception) == "width must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(2, (2,))  # tuple height"
        self.assertTrue(str(error.exception) == "height must be an integer")

        with self.assertRaises(TypeError) as error:
            Rectangle(10, 10, "string", 0)  # string x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(10, 10, 10, "string")  # string y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, [1], 0)  # list x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 10, [1])  # list y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 0.0, 0)  # float x"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 10, 0.0)  # float y"
        self.assertTrue(str(error.exception) == "y must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, (2,), 0.0)  # tuple X"
        self.assertTrue(str(error.exception) == "x must be an integer")
        with self.assertRaises(TypeError) as error:
            Rectangle(1, 1, 1, (2,))  # tuple y"
        self.assertTrue(str(error.exception) == "y must be an integer")

    def test__init__negative_numbers(self):
        """ Constructor negative numbers and zero """
        with self.assertRaises(ValueError) as error:
            Rectangle(0, 0)  # zero width"
        self.assertTrue(str(error.exception) == "width must be > 0")
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 0)  # zero height"
        self.assertTrue(str(error.exception) == "height must be > 0")
        with self.assertRaises(ValueError) as error:
            Rectangle(-10, 0)  # negative width"
        self.assertTrue(str(error.exception) == "width must be > 0")
        with self.assertRaises(ValueError) as error:
            Rectangle(10, -10)  # negative height"
        self.assertTrue(str(error.exception) == "height must be > 0")
        r = Rectangle(1, 1, 0, 0)  # zero x, y
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 10, -1)  # negative x"
        self.assertTrue(str(error.exception) == "x must be >= 0")
        with self.assertRaises(ValueError) as error:
            Rectangle(10, 10, 0, -1)  # negative x"
        self.assertTrue(str(error.exception) == "y must be >= 0")

    def test__init__instances_subclases(self):
        """ check instanciation """
        r = Rectangle(1, 1)
        self.assertTrue(isinstance(r, Rectangle))  # Rectangle instance check
        self.assertTrue(isinstance(r, Rectangle))  # Base instanciation check
        self.assertTrue(issubclass(Rectangle, Base))  # Base subclass

    def test_area(self):
        """ check area method """
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)
        r = Rectangle(2, 2)
        self.assertEqual(r.area(), 4)
        r = Rectangle(1, 1)
        self.assertEqual(r.area(), 1)

    def test_display(self):
        """ check the stdout of display """
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(4, 4)
        r1.display()
        # widht and height tests #
        self.assertEqual(output.getvalue(), "####\n####\n####\n####\n")
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(1, 1)
        r1.display()
        self.assertEqual(output.getvalue(), "#\n")
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(1, 2)
        r1.display()
        self.assertEqual(output.getvalue(), "#\n#\n")
        # axis tests #
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(1, 1, 1)
        r1.display()
        self.assertEqual(output.getvalue(), " #\n")
        output = StringIO()
        sys.stdout = output
        r1 = Rectangle(1, 2, 1, 1)
        r1.display()
        self.assertEqual(output.getvalue(), "\n #\n #\n")
        sys.stdout = sys.__stdout__

    def test__str__(self):
        """ test to __str__ method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(),  "[Rectangle] (12) 2/1 - 4/6")
        r1.height = 10
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/10")


if __name__ == "__main__":
    unittest.main()
