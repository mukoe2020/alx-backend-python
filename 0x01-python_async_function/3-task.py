#!/usr/bin/env python3
"""
function task_wait_random takes an integer max_delay and returns a asyncio.
Task
"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Args:
        max_delay (int): [description]

    Returns:
        asyncio.Task: [description]
    """
    return asyncio.create_task(wait_random(max_delay))
