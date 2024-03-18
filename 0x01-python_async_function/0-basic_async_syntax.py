#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument
    Args:
        max_delay (int, optional): integer argument. Defaults to 10.
    Returns:
        float: random float number
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
