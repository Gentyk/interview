# задачи с собеседований

### что выведет

```
import asyncio

async def my_coroutine():
    print(f"Корутина запустилась")
    await asyncio.sleep(2)
    print(f"Корутина завершена") 

async def main():
    task = asyncio.create_task(my_coroutine())
    await asyncio.sleep(1)

asyncio.run(main())
```

### яндекс 1й уровень 

```
from typing import List


def generate_thumbnail(data: bytes) -> bytes:
    """Resize image to fit a thumbnail size"""
    ...


class Connect:
    """This is an interface; you can't change it."""

    def is_ready_to_read(self) -> bool:
        """Checks if connect is ready to read"""
        ...

    def is_ready_to_write(self) -> bool:
        """Checks if connect is ready to write"""
        ...

    def read(self) -> bytes:
        """Waits until ready then reads data"""
        ...

    def write(self, data: bytes):
        """Waits until ready then writes data"""
        ...


###############################
## Code above this line can't be changed
###############################

def process(connects: List[Connect]):
    for connect in connects:
        image = connect.read()
        thumbnail = generate_thumbnail(image)
        connect.write(thumbnail)
```
нужна многопоточность*

