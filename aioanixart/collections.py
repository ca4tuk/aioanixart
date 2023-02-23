from .request_handler import AnixartRequester

from .types import AnixartCollection, AnixartRelease, AnixartComment

from .endpoints import COLLECTION, COLLECTION_RELEASES, COLLECTION_COMMENTS, SEARCH_COLLECTION

from .exceptions import AnixartAPIError


class AnixartCollections:
    def __init__(self):
        __AnixartRequester = AnixartRequester()
        self._execute = __AnixartRequester.execute

    async def view(self, collection_id: int):
        """
        Получает информацию о указанной коллекции по её ID.

        :param collection_id: ID релиза, информацию о котором нужно получить.
        :type collection_id: int

        :return: Объект AnixartCollection, содержащий информацию о запрошенной коллекции.
        :rtype: AnixartCollection

        :raises AnixartAPIError: Если коллекция с указанным ID не найдена.
        """

        response = await (await self._execute("GET", COLLECTION.format(collection_id))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанная коллекция не найдена.")

        collection = response.get("collection")
        collection["releases"] = (await self.get_releases(collection_id)).get("content")

        result = AnixartCollection(collection)
        return result

    async def get_releases(self, collection_id: int, page: int = 0):
        """
        Получает релизы указанной коллекции по её ID.

        :param collection_id: ID коллекции, для которой нужно получить релизы.
        :param page: Номер страницы коллекции (по умолчанию 0 - первая страница).

        :type collection_id: int
        :type page: int

        :return: Словарь с данными о комментариях:
                 - "content" (list) - список объектов AnixartRelease, содержащих данные о релизах;
                 - "total_count" (int) - общее количество релизов в коллекции;
                 - "total_page_count" (int) - общее количество страниц релизов коллекции;
                 - "current_page" (int) - текущая страница коллекции с релизами.

        :rtype: dict

        """

        response = await (await self._execute("GET", COLLECTION_RELEASES.format(collection_id, page))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанная коллекция не найдена.")

        result = {"content": [AnixartRelease(release) for release in response.get("content", [])],
                  "total_count": response.get("total_count"), "total_page_count": response.get("total_page_count"),
                  "current_page": response.get("current_page")}

        return result

    async def get_comments(self, collection_id: int, page: int = 0) -> dict:
        """
        Получает комментарии к указанной коллекции по её ID.

        :param collection_id: ID коллекции, для которой нужно получить комментарии.
        :param page: Номер страницы комментариев (по умолчанию 0 - первая страница).

        :type collection_id: int
        :type page: int

        :return: Словарь с данными о комментариях:
                 - "content" (list) - список объектов AnixartComment, содержащих данные о комментариях;
                 - "total_count" (int) - общее количество комментариев к коллекции;
                 - "total_page_count" (int) - общее количество страниц комментариев;
                 - "current_page" (int) - текущая страница комментариев.

        :rtype: dict

        """

        response = await (await self._execute("GET", COLLECTION_COMMENTS.format(collection_id, page))).json()
        result = {"content": [AnixartComment(comment) for comment in response.get("content", [])],
                  "total_count": response.get("total_count"), "total_page_count": response.get("total_page_count"),
                  "current_page": response.get("current_page")}

        return result

    async def search(self, query: str, page: int = 0) -> dict:
        """
        Выполняет поиск коллекций по заданному запросу.

        :param query: Строка запроса для поиска.
        :param page: Номер страницы результатов поиска (по умолчанию 0 - первая страница).

        :type query: str
        :type page: int

        :return: Словарь с данными о результатах поиска:
                 - "content" (list) - список объектов AnixartCollection, содержащих информацию о найденных коллекциях;
                 - "total_count" (int) - общее количество найденных коллекций;
                 - "total_page_count" (int) - общее количество страниц с результатами поиска;
                 - "current_page" (int) - номер текущей страницы с результатами поиска.

        :rtype: dict
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_COLLECTION.format(page), payload=payload)).json()

        result = {"content": [AnixartCollection(collection) for collection in response.get("content", [])],
                  "total_count": response.get("total_count"), "current_page": response.get("current_page"),
                  "total_page_count": response.get("total_page_count")}

        return result
