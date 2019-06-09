# loop
import asyncio

async def mycor():
    print('cor1')

@asyncio.coroutine
def mycor2():
    print("cor2")

def main():

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(mycor())
        loop.run_until_complete(mycor2())
    finally:
        loop.close()

main()