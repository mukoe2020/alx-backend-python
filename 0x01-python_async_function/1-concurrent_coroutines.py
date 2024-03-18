#!/usr/bin/env python3
"""
 write an async routine called wait_n that takes in 2 int arguments : n and max_delay 
"""
import
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    list_of_delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(list_of_delays)]

