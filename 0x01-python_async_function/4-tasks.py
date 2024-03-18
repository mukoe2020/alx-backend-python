#!/usr/bin/env python3
"""
convert wait_n to new function task_wait_n
task_wait_n is randomly being called
"""
import asyncio
from typing import List, Callable

task_wait_n = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        List[float]: [description]
    """
    list_of_delays: list[float] = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(list_of_delays)