#!/usr/bin/env python3
""" Measure runtime"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four
    times in parallel using asyncio.gather"""
    start = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    end = time.perf_counter()
    return end - start
