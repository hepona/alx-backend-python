#!/usr/bin/env python3
""" test for client"""

from client import GithubOrgClient
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """test for client"""

    def test_public_repos(self):
        """test public repos func"""

        client = GithubOrgClient("google")
        self.assertEqual(type(client.public_repos()), list)
