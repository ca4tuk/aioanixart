from aiohttp import ClientSession

from .endpoints import API_URL

from .exceptions import AnixartRequestError, AnixartAPIError


class AnixartRequester:
    def __init__(self):
        pass

    async def execute(self, method: str, endpoint: str, payload: dict = None):
        method = method.upper()

        if method == "GET":
            response = await self.get(endpoint, payload)
            return response

        elif method == "POST":
            response = await self.post(endpoint, payload)
            return response

        else:
            raise AnixartRequestError(f"Указан невалидный метод для запроса ({method}).")

    async def get(self, endpoint: str, payload: dict):
        async with ClientSession() as session:
            response = await session.get(API_URL + endpoint, json=payload)

            if not response.ok:
                raise AnixartAPIError(f"Сервер вернул отрицательный ответ: {response.status}")

            return response

    async def post(self, endpoint: str, payload: dict):
        async with ClientSession() as session:
            response = await session.post(API_URL + endpoint, json=payload)

            if not response.ok:
                raise AnixartAPIError(f"Сервер вернул отрицательный ответ: {response.status}")

            return response
