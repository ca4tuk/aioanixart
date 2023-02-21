from aioanixart import Anixart

import asyncio

anixart = Anixart()


async def main():
    # поиск пользователей
    # возвращает [], если поиск не принес результатов.
    profiles = await anixart.profile.search("ca4tuk")
    print([profile.to_dict() for profile in profiles["content"]])

    # просмотр профиля
    user_profile = await anixart.profile.view(profiles["content"][0].user_id)
    print(user_profile.to_dict())

    # просмотр истории никнеймов пользователя
    # тестовый вариант.
    user_nickname_history = await anixart.profile.nickname_history(1)
    print(user_nickname_history)

    # поиск релиза по названию
    # возвращает [], если поиск не принес результатов.
    release_search = await anixart.release.search("ИД: Вторжение")
    print([release.to_dict() for release in release_search["content"]])

    # запрос рандомного релиза
    random_release = await anixart.release.random()
    print(random_release.to_dict())

    # просмотр конкретного релиза по release_id
    # возвращает AnixartAPIError, если указанный релиз не найден.
    release = await anixart.release.view(2956)  # ID: Вторжение
    print(release.to_dict())

    # запрос комментариев релиза по release_id
    # возвращает [], если комментариев нет.
    release_comments = await anixart.release.get_comments(2956)
    print([comment.to_dict() for comment in release_comments])



if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
