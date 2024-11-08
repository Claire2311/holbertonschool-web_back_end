#!/usr/bin/env python3
"""File for testing methods in client.py
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test that GithubOrgClient.public_repos returns the correct value"""
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "mit"}},
        ]
        client = GithubOrgClient('google')

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/google/repos"
            )
            repos = client.public_repos(license="mit")
            self.assertEqual(repos, ["repo1", "repo3"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test that GithubOrgClient.has_license returns the correct value"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), expected
        )

@parameterized_class(("org_payload",
                      "repos_payload",
                      "expected_repos",
                      "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test class for GithubOrgClient.public_repos
    """
    @classmethod
    def setUpClass(cls):
        """ Setup the mocks and the patcher
        """
        mock_repos = Mock()
        mock_repos.json.return_value = cls.repos_payload
        url_map = {cls.org_payload["repos_url"]: mock_repos}

        mock_org = Mock()
        mock_org.json.return_value = cls.org_payload

        cls.get_patcher = patch("requests.get")
        cls.get_patcher.start().side_effect = lambda url: url_map.get(url,
                                                                      mock_org)

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test output of GithubOrgClient.public_repos
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("WRONG_LICENSE"), [])

    def test_public_repos_with_license(self):
        """ Test output of GithubOrgClient.public_repos with license
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
