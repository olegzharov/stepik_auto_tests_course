import asyncio

async def async_func(task_n):
    print(f'{task_n}: Запуск')
    await asyncio.sleep(1)
    print(f'{task_n}: готово!')

async def main():
    taskA = loop.create_task(async_func('A'))
    taskB = loop.create_task(async_func('B'))
    taskC = loop.create_task(async_func('C'))
    await asyncio.wait([taskA, taskB, taskC])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())