from aioanixart import Anixart

import asyncio

anixart = Anixart()


async def main():
    # Поиск пользователей:
    # возвращает dict, пользователи находятся в ключе content
    # если пользователи не найдены, ключ content будет содержать пустой список
    # 90% информации о пользователе недоступно во время поиска, поэтому для нужного пользователя после следует
    # вызвать view метод
    profiles = await anixart.profile.search("ca4tuk")
    print([profile.to_dict() for profile in profiles["content"]])

    # Просмотр профиля:
    # возвращает AnixartAPIError, если указанный пользователь не найден
    # в случае успеха возвращает AnixartUser объект.
    user_profile = await anixart.profile.view(profiles["content"][0].user_id)
    print(user_profile.to_dict())

    # просмотр истории никнеймов пользователя
    # тестовый вариант.
    user_nickname_history = await anixart.profile.nickname_history(1)
    print(user_nickname_history)

    # Поиск релиза по названию:
    # возвращает dict, релизы находятся в ключе content
    # если релизы не найдены, ключ content будет содержать пустой список
    # 90% информации о релизе недоступно во время поиска, поэтому для нужного релиза после следует вызвать view метод.
    release_search = await anixart.release.search("ИД: Вторжение")
    print([release.to_dict() for release in release_search["content"]])

    # Запрос рандомного релиза:
    # возвращает AnixartRelease
    random_release = await anixart.release.random()
    print(random_release.to_dict())

    # Просмотр конкретного релиза по release_id:
    # возвращает AnixartAPIError, если указанный релиз не найден
    # в случае успеха возвращает AnixartRelease объект.
    release = await anixart.release.view(2956)  # ID: Вторжение
    print(release.to_dict())

    # Запрос комментариев релиза по release_id:
    # возвращает dict, комментарии находятся в ключе content
    # если комментариев нет, ключ content будет содержать пустой список.
    # Также, следует подметить, что обычный просмотр релиза (будь то рандомный релиз, или конкретный по release_id),
    # возвращает не всё доступные комментарии с первой страницы, поэтому вызов этого метода не бесполезен.
    # *это касается и коллекций.
    release_comments = await anixart.release.get_comments(2956, page=1)
    print([comment.to_dict() for comment in release_comments["content"]])

    # Просмотр конкретной коллекции по collection_id:
    # возвращает AnixartAPIError, если указанная коллекция не найдена
    # в случае успеха возвращает объект AnixartCollection.
    collection = await anixart.collection.view(171892)
    print(collection.to_dict())

    # Поиск коллекции по названию:
    # возвращает dict, коллекции находятся в ключе content
    # если коллекции не найдены, ключ content будет содержать пустой список
    # 90% информации о коллекции недоступно во время поиска, поэтому
    # для нужной коллекции после следует вызвать view метод.
    collection_search = await anixart.collection.search("Валентина")
    print([collection.to_dict() for collection in collection_search["content"]])

    # Запрос списка релизов конкретной коллекции по collection_id:
    # возвращает dict с коллекциями в ключе content
    # если коллекций нет ключ content будет содержать пустой список.
    collection_releases = await anixart.collection.get_releases(171892)
    print([release.to_dict() for release in collection_releases["content"]])

    # Просмотр комментариев конкретной коллекции по collection_id:
    # возвращает dict с комментариями в ключе content
    # если комментариев нет, ключ content будет содержать пустой список.
    collection_comments = await anixart.collection.get_comments(171892)
    print([comment.to_dict() for comment in collection_comments["content"]])


if __name__ == "__main__":
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
