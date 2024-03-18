#!/usr/bin/env python3
"""
measure time function with intergers n nd max delay
"""
import random
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n
def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
      toat time / n: [description]
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n