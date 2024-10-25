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
    @patch("requests.get")
    def test_get_json(self, mock_get):
        """test the function"""
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_cases:
            # Configuration du Mock pour chaque test
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Appel de get_json et vérification des résultats
            result = get_json(test_url)
            self.assertEqual(result, test_payload)

            # Vérification que requests.get a été appelé 1 fois avec le bon URL
            mock_get.assert_called_once_with(test_url)

            # Réinitialiser le mock pour le prochain cas de test
            mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Use of Memoization"""
    def test_memoize(self):
        """test the memoize function"""
        class TestClass:
            """class to test the function"""
            def a_method(self):
                """method to test"""
                return 42

            @memoize
            def a_property(self):
                """property to test"""
                return self.a_method()

        test_instance = TestClass()
        # Vérification que la méthode est appelée la première fois
        self.assertEqual(test_instance.a_property, 42)  # 42
        # Vérification que la méthode n'est pas appelée la deuxième fois
        with patch.object(TestClass, 'a_method') as mock_method:
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_not_called()


if __name__ == "__main__":
    unittest.main()
