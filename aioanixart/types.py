class TestAnixartUser:
    """Тестовый объект пользовательского профиля, используй AnixartUser."""

    def __init__(self, profile):
        for attr in profile:
            self.__setattr__(attr, profile.get(attr))

    def to_dict(self):
        return self.__dict__


class AnixartUser:
    """Объект пользовательского профиля"""

    def __init__(self, payload):
        self.user_id = payload.get("id")
        self.login = payload.get("login")
        self.avatar = payload.get("avatar")
        self.status = payload.get("status")
        self.sponsorship_expires = payload.get("sponsorshipExpires")
        self.history = [AnixartRelease(release) for release in payload.get("history", [])]
        self.votes = payload.get("votes", [])
        self.last_activity_time = payload.get("last_activity_time")
        self.register_date = payload.get("register_date")
        self.vk_page = payload.get("vk_page")
        self.tg_page = payload.get("tg_page")
        self.inst_page = payload.get("inst_page")
        self.tt_page = payload.get("tt_page")
        self.discord_page = payload.get("discord_page")
        self.ban_expires = payload.get("ban_expires")
        self.ban_reason = payload.get("ban_reason")
        self.ban_note = payload.get("ban_note")
        self.privilege_level = payload.get("privilege_level")
        self.is_private = payload.get("is_private")
        self.is_sponsor = payload.get("is_sponsor")
        self.is_banned = payload.get("is_banned")
        self.is_perm_banned = payload.get("is_perm_banned")
        self.is_verified = payload.get("is_verified")
        self.rating_score = payload.get("rating_score")
        self.is_online = payload.get("is_online")
        self.roles = payload.get("roles")

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)


class AnixartRelease:
    """Объект релиза"""

    def __init__(self, payload):
        self.release_id = payload.get("id")
        self.poster = payload.get("poster")
        self.poster_image = payload.get("image")
        self.year = payload.get("year")
        self.genres = payload.get("genres")
        self.country = payload.get("country")
        self.director = payload.get("director")
        self.studio = payload.get("studio")
        self.author = payload.get("author")
        self.translators = payload.get("translators")
        self.description = payload.get("description")
        self.category_id = payload.get("category", {}).get("id")
        self.category_name = payload.get("category", {}).get("name")
        self.rating = payload.get("grade")
        self.status_id = payload.get("status", {}).get("id")
        self.status_name = payload.get("status", {}).get("name")
        self.duration = payload.get("duration")
        self.season = payload.get("season")
        self.screenshots = payload.get("screenshots")
        self.screenshot_images = payload.get("screenshot_images")
        self.title_original = payload.get("title_original")
        self.title_ru = payload.get("title_ru")
        self.title_alt = payload.get("title_alt")
        self.episodes_total = payload.get("episodes_total")
        self.episodes_released = payload.get("episodes_released")
        self.release_date = payload.get("release_date")
        self.creation_date = payload.get("creation_date")
        self.last_update_date = payload.get("last_update_date")
        self.is_adult = payload.get("is_adult")
        self.age_rating = payload.get("age_rating")
        self.recommended_releases = payload.get("recommended_releases")
        self.collection_count = payload.get("collection_count")
        self.comments = [AnixartComment(comment) for comment in payload.get("comments", [])]

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)


class AnixartComment:
    """Объект комментария"""

    def __init__(self, payload):
        self.comment_id = payload.get("id")
        self.author = AnixartUser(payload.get("profile"))
        self.message = payload.get("message")
        self.timestamp = payload.get("timestamp")
        self.likes_count = payload.get("likes_count")
        self.is_spoiler = payload.get("is_spoiler")

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)


class AnixartCollection:  # TODO: *
    """Объект коллекции"""

    def __init__(self):
        pass
