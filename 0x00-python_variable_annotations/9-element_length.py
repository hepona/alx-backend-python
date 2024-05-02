#!/usr/bin/env python3
"""element length"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate the below function's parameters and
    return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
