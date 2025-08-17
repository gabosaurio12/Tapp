class Profile:
    def __init__(
            self,
            id_profile: int = 0,
            username: str = "",
            password: str = "",
            name: str = "",
            schedules: list = None
    ):
        self.__id_profile = id_profile
        self.__username = username
        self.__password = password
        self.__name = name
        self.__schedules = schedules if schedules is not None else []

    @property
    def id_profile(self):
        return self.__id_profile

    @id_profile.setter
    def id_profile(self, id_profile):
        self.__id_profile = id_profile

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def schedules(self):
        return self.__schedules

    @schedules.setter
    def schedules(self, schedules):
        self.__schedules = schedules

    def to_clean_dict(self):
        return {
            "id_profile": self.id_profile,
            "username": self.username,
            "password": self.password,
            "name": self.name
        }