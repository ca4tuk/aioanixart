from .profile import AnixartProfiles
from .release import AnixartReleases
from .collections import AnixartCollections


class Anixart:
    """
    Anixart API class object.
    """

    def __init__(self):
        self.__profile = AnixartProfiles()
        self.__release = AnixartReleases()
        self.__collection = AnixartCollections()

    @property
    def profile(self):
        return self.__profile

    @property
    def release(self):
        return self.__release

    @property
    def collection(self):
        return self.__collection
