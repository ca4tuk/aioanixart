from .request_handler import AnixartRequester

from .types import AnixartUser

from .endpoints import PROFILE, SEARCH_PROFILE, PROFILE_NICK_HISTORY

from .exceptions import AnixartAPIError


class AnixartProfiles:
    def __init__(self):
        __AnixartRequester = AnixartRequester()
        self._execute = __AnixartRequester.execute

    async def view(self, user_id: int) -> AnixartUser:
        """
        Возвращает объект AnixartUser, содержащий информацию о пользователе с указанным идентификатором.

        :param user_id: Целочисленный идентификатор пользователя.
        :type user_id: int

        :return: Объект AnixartUser, содержащий информацию о пользователе.
        :rtype: AnixartUser

        :raises AnixartAPIError: Если пользователь с указанным идентификатором не найден.
        """

        response = await (await self._execute("GET", PROFILE.format(user_id))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанный пользователь не найден.")
        result = AnixartUser(response.get("profile"))

        return result

    async def nickname_history(self, user_id: int, page: int = 0) -> dict:  # TODO: rework
        """не используйте это пж"""

        response = await (await self._execute("GET", PROFILE_NICK_HISTORY.format(user_id, page))).json()
        return response

    async def search(self, query: str, page: int = 0) -> dict:
        """
        Поиск пользователей по заданному запросу.

        :param query: Строка запроса.
        :type query: str

        :param page: Номер страницы с результатами поиска.
        :type page: int

        :return: Словарь, содержащий список найденных пользователей, общее количество найденных пользователей,
                 текущую страницу и общее количество страниц с результатами.
        :rtype: dict
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_PROFILE.format(page), payload=payload)).json()

        result = {"content": [AnixartUser(user) for user in response.get("content", [])],
                  "total_count": response.get("total_count"), "current_page": response.get("current_page"),
                  "total_page_count": response.get("total_page_count")}

        return result
