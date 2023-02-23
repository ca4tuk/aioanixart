from .request_handler import AnixartRequester

from .types import AnixartRelease, AnixartComment

from .endpoints import SEARCH_RELEASE, RELEASE_RANDOM, RELEASE, RELEASE_COMMENTS

from .exceptions import AnixartAPIError


class AnixartReleases:
    def __init__(self):
        __AnixartRequester = AnixartRequester()
        self._execute = __AnixartRequester.execute

    async def search(self, query: str, page: int = 0) -> dict:
        """
        Выполняет поиск релизов по заданному запросу.

        :param query: Строка запроса для поиска.
        :param page: Номер страницы результатов поиска (по умолчанию 0 - первая страница).

        :type query: str
        :type page: int

        :return: Словарь с данными о результатах поиска:
                 - "content" (list) - список объектов AnixartRelease, содержащих информацию о найденных релизах;
                 - "total_count" (int) - общее количество найденных релизов;
                 - "total_page_count" (int) - общее количество страниц с результатами поиска;
                 - "current_page" (int) - номер текущей страницы с результатами поиска.

        :rtype: dict
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_RELEASE.format(page), payload=payload)).json()

        result = {"content": [AnixartRelease(release) for release in response.get("content")],
                  "total_count": response.get("total_count"), "current_page": response.get("current_page"),
                  "total_page_count": response.get("total_page_count")}

        return result

    async def random(self) -> AnixartRelease:
        """
        Получает информацию о случайном релизе.

        :return: Объект AnixartRelease, содержащий информацию о случайном релизе.
        :rtype: AnixartRelease

        """

        response = await (await self._execute("GET", RELEASE_RANDOM)).json()
        result = AnixartRelease(response.get("release"))

        return result

    async def view(self, release_id: int) -> AnixartRelease:
        """
        Получает информацию о указанном релизе по его ID.

        :param release_id: ID релиза, информацию о котором нужно получить.
        :type release_id: int

        :return: Объект AnixartRelease, содержащий информацию о запрошенном релизе.
        :rtype: AnixartRelease

        :raises AnixartAPIError: Если релиз с указанным ID не найден.
        """

        response = await (await self._execute("GET", RELEASE.format(release_id))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанный релиз не найден.")

        result = AnixartRelease(response.get("release"))

        return result

    async def get_comments(self, release_id: int, page: int = 0) -> dict:
        """
        Получает комментарии указанного релиза по его ID.

        :param release_id: ID релиза, для которого нужно получить комментарии.
        :param page: Номер страницы комментариев (по умолчанию 0 - первая страница).

        :type release_id: int
        :type page: int

        :return: Словарь с данными о комментариях:
                 - "content" (list) - список объектов AnixartComment, содержащих данные о комментариях;
                 - "total_count" (int) - общее количество комментариев к релизу;
                 - "total_page_count" (int) - общее количество страниц комментариев;
                 - "current_page" (int) - текущая страница комментариев.

        :rtype: dict

        """

        response = await (await self._execute("GET", RELEASE_COMMENTS.format(release_id, page))).json()
        result = {"content": [AnixartComment(comment) for comment in response.get("content", [])],
                  "total_count": response.get("total_count"), "total_page_count": response.get("total_page_count"),
                  "current_page": response.get("current_page")}

        return result
