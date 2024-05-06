#!/usr/bin/env python3
"""0. The basics of async"""
import random
import asyncio
from typing import Union


async def wait_random(max_delay: int = 10):
    """takes in an integer argument
    that waits for a random delay between 0 and"""
    wait = random.randrange(0, max_delay)
    await asyncio.sleep(wait)
    return wait
