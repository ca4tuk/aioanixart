from .profile import AnixartProfile
from .release import AnixartReleases


class Anixart:
    """
    Anixart API class object.
    """

    def __init__(self):
        self.__profile = AnixartProfile()
        self.__release = AnixartReleases()

    @property
    def profile(self):
        return self.__profile

    @property
    def release(self):
        return self.__release
