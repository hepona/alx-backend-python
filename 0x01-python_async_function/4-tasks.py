#!/usr/bin/env python3
"""4-tasks"""
import asyncio as asy
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn task_wait_random n times with the specified max_delay."""
    data = []
    for _ in range(n):
        data.append(await task_wait_random(max_delay))
    return sorted(data)
