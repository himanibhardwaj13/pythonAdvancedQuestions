import asyncio
import time
# sleep: pauses a coroutine without blocking the entire program.
# run: This starts the event loop and executes the top-level async function.
# gather: Runs multiple coroutines concurrently and waits for all of them.

async def perform_task1():
  print("Task1 started")
  await  asyncio.sleep(2)
  print("Task1 is performed")

async def perform_task2():
  print("Task2 started")
  await  asyncio.sleep(3)
  print("Task2 is performed")
  
# without gather function
async def main_without():
    start = time.perf_counter()
    await perform_task1()
    await perform_task2()
    end = time.perf_counter()
    print(f"{end-start:.2f} sec")

# with gather function
async def main_with():
    start = time.perf_counter()
    await asyncio.gather(perform_task1(), perform_task2())
    end = time.perf_counter()
    print(f"{end-start:.2f} sec")
  
# Execution
asyncio.run(main_without())
asyncio.run(main_with())
