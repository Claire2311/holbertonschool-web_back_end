#!/usr/bin/env python3
"""
function that take a list as argument
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list"""
    return [(i, len(i)) for i in lst]
