#!/usr/bin/env python3
"""safely get value"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(
    dct: Mapping, key: Any, default: Union[TypeVar, None] = None
) -> Union[Any, Union[Any, TypeVar]]:
    """Given the parameters and the return values,
    add type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
