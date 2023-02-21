from aioanixart import Anixart

import asyncio

anixart = Anixart()


async def main():
    # запрос профиля
    user_profile = await anixart.profile.view(1)
    print(user_profile.to_dict())

    # запрос истории никнеймов пользователя
    user_nickname_history = await anixart.profile.nickname_history(1)
    print(user_nickname_history)

    # поиск релиза по названию
    search = await anixart.release.search("ID Вторжение")
    print([release.to_dict() for release in search["content"]])

    # запрос рандомного релиза
    random_release = await anixart.release.random()
    print(random_release.to_dict())


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
