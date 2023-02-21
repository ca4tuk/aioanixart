from .request_handler import AnixartRequester

from .types import AnixartRelease, AnixartComment

from .endpoints import SEARCH_RELEASE, RELEASE_RANDOM, RELEASE, RELEASE_COMMENTS

from .exceptions import AnixartAPIError


class AnixartReleases:
    def __init__(self):
        __AnixartRequester = AnixartRequester()
        self._execute = __AnixartRequester.execute

    async def search(self, query: str, page: int = 0):
        """
        :param query: search query
        :param page: page count

        :type query: str
        :type page: int

        :return: dict
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_RELEASE.format(page), payload=payload)).json()

        result = {"content": [], "total_count": response.get("total_count"),
                  "current_page": response.get("current_page"), "total_page_count": response.get("total_page_count")}

        for release in response.get("content", []):
            result["content"].append(AnixartRelease(release))

        return result

    async def random(self):
        """
        :return: AnixartRelease
        """

        response = await (await self._execute("GET", RELEASE_RANDOM)).json()
        result = AnixartRelease(response.get("release"))

        return result

    async def view(self, release_id: int):
        """

        :param release_id: release_id

        :type release_id: int

        :return: AnixartRelease
        """

        response = await (await self._execute("GET", RELEASE.format(release_id))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанный релиз не найден.")

        result = AnixartRelease(response.get("release"))

        return result

    async def get_comments(self, release_id: int, page: int = 0):
        """
        :param release_id: release id
        :param page: comment page

        :type release_id: int
        :type page: int

        :return: list
        """

        response = await (await self._execute("GET", RELEASE_COMMENTS.format(release_id, page))).json()
        result = [AnixartComment(comment) for comment in response.get("content", [])]

        return result
