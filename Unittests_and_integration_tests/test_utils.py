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

    # Ma proposition qui est passée sur le cheker
    # @parameterized.expand([
    #     ({}, ("a"), None),
    #     ({"a": 1}, ("a", "b"), None),
    # ])
    # def test_access_nested_map_exception(self, nested_map, path, expected):
    #     """test the raising of error of the func"""
    #     if expected is None:
    #         with self.assertRaises(KeyError):
    #             access_nested_map(nested_map, path)

    # Solution proposée par ChatGPT
    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test the raising of error of the func"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        # On vérifie que le msg de l'exception correspond à la clé manquante
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
