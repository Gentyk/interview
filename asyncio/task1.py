# Coroutines and Tasks
import asyncio
import time


async def pause_output(pause, msg):
    await asyncio.sleep(pause)
    if not msg:
        raise Exception
    print(msg)


async def pause_return(pause, msg):
    await asyncio.sleep(pause)
    return msg


async def stop(pause):
    await asyncio.sleep(pause)


async def example1():
    # последовательный запуск сопрограмм (2 сек)
    print(f"started at {time.strftime('%X')}")
    await pause_output(1, "good")
    await pause_output(2, "boy")
    print(f"finished at {time.strftime('%X')}")

    # формируем в задачи и запускаем параллельно(3 сек)
    task1 = asyncio.create_task(pause_output(1, "nice"))
    task2 = asyncio.create_task(pause_output(2, "girl"))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


async def example2():
    # одновременное выполнение задач и эксперимент с ошибкми
    task1 = asyncio.create_task(pause_output(1, "nice"))
    task2 = asyncio.create_task(pause_output(1, "сorgi"))
    task3 = asyncio.create_task(pause_output(0.1, None))
    task4 = asyncio.create_task(pause_output(1, "сorgi2"))
    task4.cancel()
    print(f"started at {time.strftime('%X')}")
    print(await asyncio.gather(task1, task2, task3, task4, return_exceptions=True))
    print(f"finished at {time.strftime('%X')}")


async def example3():
    # рассматриваются wait_for и  wait
    try:
        await asyncio.wait_for(stop(20), timeout=1)
    except asyncio.TimeoutError:
        print("funny")

    task1 = asyncio.create_task(pause_output(0.1, "wait1"))
    courutine1 = stop(0.1)
    done, pending = await asyncio.wait(
        {courutine1, task1}, return_when=asyncio.ALL_COMPLETED
    )
    print(pending)


async def example4():
    # asyncio.as_completed
    aws = {
        pause_return(1, 1),
        pause_return(3, 3),
        pause_return(2, 2),
    }
    print(f"started at {time.strftime('%X')}")
    for f in asyncio.as_completed(aws):
        earliest_result = await f
        print(earliest_result)
    print(f"finished at {time.strftime('%X')}")


async def monit():
    print(asyncio.current_task())
    for task in asyncio.all_tasks():
        print(task)


async def example5():
    # проверка самоанализа
    task1 = asyncio.create_task(pause_output(2, "task1"))
    task2 = asyncio.create_task(pause_output(1, "task2"))
    print(await asyncio.gather(task1, task2, monit(), return_exceptions=True))


async def example6():
    # просто анализ задачи
    task1 = asyncio.create_task(pause_return(0.2, "task1"))
    await task1
    print(task1.result())
    task1.print_stack()


async def main():
    await example6()


asyncio.run(main())
