from aioanixart import Anixart

import asyncio

anixart = Anixart()


async def main():
    search = await anixart.release.search(query="бог")
    print(search)


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
