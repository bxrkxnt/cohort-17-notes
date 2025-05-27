"""
async - switch between tasks very quickly
parallel / concurrent - do them both at the same time
"""

import asyncio
from asyncio import sleep

async def main(process_number: int):
    print(f"Starting function {process_number}")
    await sleep(2) # like a requests.get()
    print(f"Finished process {process_number}")

async def run_tasks():
    async with asyncio.TaskGroup() as tg:
        for i in range(10):
            tg.create_task(main(i))


asyncio.run(run_tasks())