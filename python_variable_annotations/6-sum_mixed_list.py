#!/usr/bin/env python3
"""
function that a list of floats and integer as argument and returns their sum
>>> sum_mixed_list([5, 4, 3.14, 666, 0.99])
679.13
"""

from typing import List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """return the sum of floats and integer"""
    a = 0
    for number in mxd_lst:
        a += number
    return a
