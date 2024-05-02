#!/usr/bin/env python3
"""element length"""
from typing import  List, Tuple, Any
from collections.abc import Iterable

def element_length(lst: Iterable) -> Tuple[Any]:
    """doc"""
    return [(i, len(i)) for i in lst]
