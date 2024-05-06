#!/usr/bin/env python3
""""""
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """spawn wait_random n times with the specified max_delay."""
    lst = []
    for _ in range(1, n):
        wait_random(max_delay)
        lst.append(wait_random(max_delay))
    return lst
