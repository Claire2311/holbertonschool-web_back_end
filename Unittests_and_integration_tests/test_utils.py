#!/usr/bin/env python3
"""File for testing
"""

import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
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


class TestGetJson(unittest.TestCase):
    """class to test the get_json func"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test the get_json function"""
        with patch.object("utils.resquests.get") as mock_get_json:
            mock_return = Mock()
            mock_return.json.return_value = test_payload
            mock_get_json.return_value = mock_return

            self.assertEqual(get_json(test_url), test_payload)
            mock_get_json.assert_called_once_with(test_url)


    # @patch("requests.get")
    # def test_get_json(self, mock_get):
    #     """test the function"""
    #     test_cases = [
    #         ("http://example.com", {"payload": True}),
    #         ("http://holberton.io", {"payload": False})
    #     ]

    #     for test_url, test_payload in test_cases:
    #         # Configuration du Mock pour chaque test
    #         mock_response = Mock()
    #         mock_response.json.return_value = test_payload
    #         mock_get.return_value = mock_response

    #         # Appel de get_json et vérification des résultats
    #         result = get_json(test_url)
    #         self.assertEqual(result, test_payload)

    #         # Vérification que requests.get a été appelé 1 fois avec le bon URL
    #         mock_get.assert_called_once_with(test_url)

    #         # Réinitialiser le mock pour le prochain cas de test
    #         mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""
    def test_memoize(self):
        """Test that the memoize decorator caches the result of a method"""

        class TestClass:
            """Class to test the memoize decorator"""

            def a_method(self):
                """Method to be memoized"""
                return 42

            @memoize
            def a_property(self):
                """Property that uses the memoize decorator"""
                return self.a_method()

        # Patch the a_method to ensure it is only called once
        with patch.object(TestClass,
                          "a_method",
                          return_value=42) as mock_method:
            test_obj = TestClass()

            # Call the memoized property twice
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            # Check that the results are as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure that a_method was only called once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
