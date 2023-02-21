from .request_handler import AnixartRequester

from .types import AnixartUser

from .endpoints import PROFILE, SEARCH_PROFILE, PROFILE_NICK_HISTORY


class AnixartProfile:
    def __init__(self):
        __AnixartRequester = AnixartRequester()
        self._execute = __AnixartRequester.execute

    async def view(self, user_id: int) -> AnixartUser:
        """
        :param user_id:
        :return:
        """

        response = await (await self._execute("GET", PROFILE.format(user_id))).json()
        result = AnixartUser(response.get("profile"))

        return result

    async def nickname_history(self, user_id: int, page: int = 0) -> dict:  # TODO: *
        """
        :param user_id: user_id
        :param page: page_number

        :type user_id: int
        :type page: int
        :return:
        """

        response = await (await self._execute("GET", PROFILE_NICK_HISTORY.format(user_id, page))).json()
        return response

    async def search(self, query: str, page: int = 0):
        """

        :param query: search query
        :param page: page count
        :return:
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_PROFILE.format(page), payload=payload)).json()

        result = {"content": [], "total_count": response.get("total_count"),
                  "current_page": response.get("current_page"), "total_page_count": response.get("total_page_count")}

        for user in response.get("content"):
            result["content"].append(AnixartUser(user))

        return result
