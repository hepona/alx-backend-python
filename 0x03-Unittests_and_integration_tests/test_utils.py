#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from parameterized import parameterized


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


if __name__ == "__main__":
    unittest.main()
