#!/usr/bin/env python3
"""
write a coroutine thats takes no arguments
"""
import random
import asyncio


async def async_generator():-> Generator[None, None, None]:
    """
    coroutine that takes no arguments
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
