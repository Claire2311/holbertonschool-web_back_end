#!/usr/bin/env python3
"""File for testing methods in client.py
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """unittest class to implement test for client.py"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """
        test that GithubOrgClient._public_repos_url returns the correct value
        """
        client = GithubOrgClient('google')

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            # Définir la valeur que vous voulez pour le test
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            # Vérifiez que la valeur mockée est retournée
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/orgs/google/repos"
            )
