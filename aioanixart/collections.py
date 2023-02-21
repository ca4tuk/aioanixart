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
        :param collection_id: collection id
        :type collection_id: int
        :return: dict
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
        :param collection_id: collection id
        :param page: page number
        :type collection_id: int
        :type page: int
        :return: dict
        """

        response = await (await self._execute("GET", COLLECTION_RELEASES.format(collection_id, page))).json()
        if response.get("code") != 0:
            raise AnixartAPIError("Указанная коллекция не найдена.")

        result = {"content": [AnixartRelease(release) for release in response.get("content", [])],
                  "total_count": response.get("total_count"), "total_page_count": response.get("total_page_count"),
                  "current_page": response.get("current_page")}

        return result

    async def get_comments(self, collection_id: int, page: int = 0):
        """

        :param collection_id: collection id
        :param page: page number
        :type collection_id: int
        :type page: int
        :return: dict
        """

        response = await (await self._execute("GET", COLLECTION_COMMENTS.format(collection_id, page))).json()
        result = {"content": [AnixartComment(comment) for comment in response.get("content", [])],
                  "total_count": response.get("total_count"), "total_page_count": response.get("total_page_count"),
                  "current_page": response.get("current_page")}

        return result

    async def search(self, query: str, page: int = 0):
        """

        :param query: search query
        :param page: page count
        :return:
        """

        payload = {"query": query, "searchBy": 0}
        response = await (await self._execute("POST", SEARCH_COLLECTION.format(page), payload=payload)).json()

        result = {"content": [AnixartCollection(collection) for collection in response.get("content", [])],
                  "total_count": response.get("total_count"), "current_page": response.get("current_page"),
                  "total_page_count": response.get("total_page_count")}

        return result
