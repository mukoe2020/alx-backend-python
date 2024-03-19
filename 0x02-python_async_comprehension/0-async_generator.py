#!/usr/bin/env python3
"""
write a coroutine thats takes no arguments
"""
import random
import asyncio


async def async_generator():
    """
    it will loop 10 time
    and yeild a random number between 0 and 10
    """
    for in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
