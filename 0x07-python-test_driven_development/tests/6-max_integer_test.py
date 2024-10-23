#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_positive_integers(self):
        """Test with a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_integers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 0, 3, -4]), 3)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.5, 2.7, 0.3, 3.9]), 3.9)

    def test_list_with_one_element(self):
        """Test with a list that contains only one element"""
        self.assertEqual(max_integer([10]), 10)

    def test_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none(self):
        """Test with None passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list(self):
        """Test with a non-list argument"""
        with self.assertRaises(TypeError):
            max_integer(123)

if __name__ == '__main__':
    unittest.main()

