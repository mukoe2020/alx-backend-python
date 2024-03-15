#!/usr/bin/env python3
"""
Annotate  function’s parameters and return values with the appropriate types
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Sequence[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns list of tuples containing length of each element and element itself
    """
    return [(i, len(i)) for i in lst]
