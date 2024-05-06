#!/usr/bin/env python3
"""2. Measure the runtime"""
wait_n = __import__("1-concurrent_coroutine").wait_n
import time

def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)"""
    