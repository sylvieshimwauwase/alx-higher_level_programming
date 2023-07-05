#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):

    def test_max_integer_positive_numbers(self):
        """Test max_integer function with positive numbers"""
        nums = [1, 2, 3, 4, 5]
        result = max_integer(nums)
        self.assertEqual(result, 5)

    def test_max_integer_negative_numbers(self):
        """Test max_integer function with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        result = max_integer(nums)
        self.assertEqual(result, -1)

    def test_max_integer_mixed_numbers(self):
        """Test max_integer function with mixed positive and negative numbers"""
        nums = [1, -2, 3, -4, 5]
        result = max_integer(nums)
        self.assertEqual(result, 5)

    def test_max_integer_empty_list(self):
        """Test max_integer function with an empty list"""
        nums = []
        result = max_integer(nums)
        self.assertIsNone(result)

    def test_max_integer_duplicate_numbers(self):
        """Test max_integer function with duplicate numbers"""
        nums = [1, 1, 1, 1, 1]
        result = max_integer(nums)
        self.assertEqual(result, 1)

    def test_max_integer_single_number(self):
        """Test max_integer function with a single number"""
        nums = [10]
        result = max_integer(nums)
        self.assertEqual(result, 10)

    def test_max_integer_no_numbers(self):
        """Test max_integer function with a list containing non-numeric elements"""
        nums = ['a', 'b', 'c']
        self.assertRaises(TypeError, max_integer, nums)


if __name__ == '__main__':
    unittest.main()
