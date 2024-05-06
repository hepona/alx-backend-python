#!/usr/bin/env python3
""" 3-task"""
import asyncio as asy

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asy.Task:
    """takes an integer max_delay and returns a asyncio.Task"""
    return asy.create_task(wait_random(max_delay))
