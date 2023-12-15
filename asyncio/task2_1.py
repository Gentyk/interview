# loop
import asyncio
import random


async def mycor(id_):
    time_ = 0.1 * random.randint(1, 5)
    await asyncio.sleep(time_)
    print(id_, time_)


async def infinite_cor():
    while True:
        time_ = 0.1 * random.randint(1, 5)
        await asyncio.sleep(time_)
        print(time_)


async def main(loop):
    tasks = []
    for i in range(4):
        tasks.append(asyncio.create_task(mycor(i)))
    await asyncio.gather(*tasks)
    print(asyncio.Task.all_tasks())
    loop.stop()


loop = asyncio.get_event_loop()
try:
    # вариант 1
    # loop.run_until_complete(main())

    # вариант 2
    asyncio.ensure_future(main(loop))
    # asyncio.ensure_future(infinite_cor())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
