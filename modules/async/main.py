import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_message() -> str:
    await delay(2)
    return 'Hello World!'


async def pure_sequential():
    msg = await hello_message()
    # Sequential bcoz await pauses our current coroutine and won’t execute any
    # other code inside that coroutine until the await expression gives us a value.
    plus1 = await add_one(1)
    print(plus1)
    print(msg)


async def create_task_demo1():


async def main():
    await pure_sequential()


asyncio.run(main())
