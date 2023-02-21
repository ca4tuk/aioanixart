from .request_handler import AnixartRequester

from .types import AnixartUser

from .endpoints import PROFILE, PROFILE_NICK_HISTORY


class AnixartProfileBase(AnixartRequester):
    def __init__(self):
        super(AnixartProfileBase, self).__init__()
        self._execute = super().execute


class AnixartProfile(AnixartProfileBase):
    def __init__(self):
        super(AnixartProfile, self).__init__()

    async def view(self, user_id: int) -> AnixartUser:
        """
        :param user_id:
        :return:
        """
        response = await (await self._execute("GET", PROFILE.format(user_id))).json()
        return AnixartUser(response.get("profile"))

    async def nickname_history(self, user_id: int, page: int = 0) -> dict:
        """
        :param user_id: user_id
        :param page: page_number

        :type user_id: int
        :type page: int
        :return:
        """

        response = await (await self._execute("GET", PROFILE_NICK_HISTORY.format(user_id, page))).json()
        return response
