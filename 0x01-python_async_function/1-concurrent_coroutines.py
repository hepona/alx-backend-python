#!/usr/bin/env python3
"""concurrent coroutines"""
import asyncio as asy

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """spawn wait_random n times with the specified max_delay."""
    data = []
    for _ in range(n):
        data.append(await asy.gather(wait_random(max_delay)))
    return data
