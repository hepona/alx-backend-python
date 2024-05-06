#!/usr/bin/env python3
"""concurrent coroutines"""
import asyncio as asy
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    data = []
    for _ in range(n):
        res = asy.create_task(wait_random(max_delay))
        data.append(await res)
    return sorted(data)
