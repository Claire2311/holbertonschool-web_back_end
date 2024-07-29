#!/usr/bin/env python3
"""
function that returns element of a dictionnary
"""

from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar, None]
                     = None):
    """function that returns element of a dictionnary"""
    if key in dct:
        return dct[key]
    else:
        return default
