#!/usr/bin/env python3
"""0. The basics of async"""
import random
import asyncio


async def wait_random(max_delay=10):
    """takes in an integer argument
    that waits for a random delay between 0 and max_delay"""
    wait = random.randrange(0, max_delay)
    await asyncio.sleep(wait)
    return wait
