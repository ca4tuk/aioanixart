from .profile import AnixartProfile
from .release import AnixartReleases


class Anixart:
    def __init__(self):
        self.me = None
        self.__profile = AnixartProfile()
        self.__release = AnixartReleases()

    @property
    def profile(self):
        return self.__profile

    @property
    def release(self):
        return self.__release
