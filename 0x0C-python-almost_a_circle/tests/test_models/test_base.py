#!/usr/bin/python3
"""unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class Test_Base(unittest.TestCase):
    """Defining class to evaluate test cases for base.py"""

    def test_with_id(self):
        """checking instance of the class"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))

    def test_with_none_id(self):
        """checking when id is none"""
        b1 = Base(id=1)
        self.assertEqual(b1.id, 1)
        b1 = Base(id=3)
        self.assertEqual(b1.id, 3)

    def test_with_none_id_increment(self):
        """checking if id increment correctly"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_value(self):
        """testing value of id"""
        b1 = Base(50)
        self.assertEqual(b1.id, 50)
        b1 = Base(-7)
        self.assertEqual(b1.id, -7)
        b1 = Base(0)
        self.assertEqual(b1.id, 0)
        b1 = Base(1000e+1000)
        self.assertEqual(b1.id, 1000e+1000)
        b1.__init__(4)
        self.assertEqual(b1.id, 4)

    def test_obj_attributes(self):
        """testing objects attributes"""
        b1 = Base()
        self.assertEqual(b1.__dict__, {'id': 1})
        b2 = Base(90)
        self.assertEqual(b2.__dict__, {'id': 90})

    def test_errors_raises(self):
        """testing on errors raises"""
        self.assertRaises(TypeError)
        b1 = Base(id="Invalid_id")
        self.assertRaises(AttributeError)
        b1.to_dictionary()
        self.assertRaises(NameError)
        b1.Base()

    def test_json_string(self):
        """testing for json string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dict = r1.to_dictionary()
        json_dict = Base.to_json_string(sorted(dict.items()))
        self.assertEqual(json_dict, '[["height",7], ["id", 30], '
                         ' ["width", 10], ["x", 2], ["y", 8]]')
        self.assertTrue(type(dict) != type(json_dict))

        r1 = Rectangle(50, 40)
        dict = r1.to_dictionary()
        json_dict = Base.to_json_string(sorted(dict.items()))
        self.assertEqual(json_dict, '[["height",40], ["id", 2], '
                         ' ["width", 50], ["x", 0], ["y", 0]]')
        self.assertTrue(type(dict) != type(json_dict))

        dict = []
        json_dict = Base.to_json_string(dict)
        self.assertEqual(json_dict, '[]')
        self.assertTrue(type(dict) != type(json_dict))

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
