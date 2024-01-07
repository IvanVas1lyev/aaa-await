import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float) -> None:
    task = asyncio.create_task(coro)
    await asyncio.wait_for(task, timeout=max_execution_time)


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    tasks = [asyncio.create_task(coro) for coro in coros]
    done, ndone = await asyncio.wait(tasks, timeout=max_execution_time)

    for task in ndone:
        task.cancel()

