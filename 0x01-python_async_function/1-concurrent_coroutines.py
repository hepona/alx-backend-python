#!/usr/bin/env python3
""""""
import asyncio as asy

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """spawn wait_random n times with the specified max_delay."""
    lst = []
    for _ in range(1, n):
        data = wait_random(max_delay)
        await asy.sleep(data)
        lst.append(data)
    return lst
