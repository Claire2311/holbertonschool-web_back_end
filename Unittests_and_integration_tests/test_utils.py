#!/usr/bin/env python3
"""File for testing
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """unittest class to design all tests"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test the access_nested_map func"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), None),
        ({"a": 1}, ("a", "b"), None),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """test the raising of error of the func"""
        if expected is None:
            with self.assertRaises(KeyError):
                access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
