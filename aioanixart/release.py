from .request_handler import AnixartRequester

from .types import AnixartRelease

from .endpoints import SEARCH_RELEASE, RELEASE_RANDOM


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

        :return: list
        """

        result = []

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_RELEASE.format(page), payload=payload)).json()

        for release in response.get("content", []):
            result.append(AnixartRelease(release))

        return result

    async def random(self):
        """
        :return: AnixartRelease
        """

        response = await (await self._execute("GET", RELEASE_RANDOM)).json()
        response = AnixartRelease(response.get("release"))

        return response
