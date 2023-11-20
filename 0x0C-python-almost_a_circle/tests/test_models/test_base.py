#!/usr/bin/python3
""" Base test suit """
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class Base_test(unittest.TestCase):
    """ Test base class """

    def test_pep8(self):
        """ pep8 test """
        pep8style = pep8.StyleGuide(quiet=True)
        output = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(output.total_errors, 0)

    def test_constructor(self):
        """ consrtuctor test """
        b1 = Base()
        self.assertTrue(b1.id == 1)
        b2 = Base()
        self.assertTrue(b2.id == 2)
        b3 = Base(4)
        self.assertTrue(b3.id == 4)
        b4 = Base()
        self.assertTrue(b4.id == 3)
        b5 = Base(None)
        self.assertTrue(b5.id == 4)
    
    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")



if __name__ == "__main__":
    unittest.main()
