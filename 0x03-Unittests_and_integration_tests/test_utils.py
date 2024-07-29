#!/usr/bin/env python3
"""Utils.py 's test"""
import unittest
from unittest import mock
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from parameterized import parameterized
import requests


class TestAccessNestedMap(unittest.TestCase):
    """class test Access nested map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, excepted: Any
    ) -> None:
        """check if the func return what it's supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), excepted)

    @parameterized.expand([({}, ("a",), None), ({"a": 1}, ("a", "b"), None)])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, excepted: Any
    ) -> None:
        """test exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class test for testgetjson func"""

    @patch("requests.get()")
    @parameterized.expand(
        [
            (
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
            )
        ]
    )
    def test_get_json(self, test_url: str, test_payload: Dict, mock: Mock) -> None:
        """test get_json func"""
        mock.return_value.json.return_value = test_payload
        mock.assert_called_once_with(test_url)
        self.assertEqual(test_url, test_payload)


if __name__ == "__main__":
    unittest.main()
