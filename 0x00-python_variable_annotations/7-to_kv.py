#!/usr/bin/env python3
"""type-annotated function to_kv """
from typing import Union, Tuple


def to_kv(
    k: str,
    v: Union[int, float],
) -> Tuple[str, float]:
    """takes a string k and an int OR
    float v as arguments and returns a tuple."""
    return (k, v**2)
