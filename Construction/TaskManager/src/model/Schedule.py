class Schedule:
    def __init__ (
            self,
            id_schedule: int,
            tasks: list,
            id_profile: int
    ):
        self._id_schedule = id_schedule
        self._tasks = tasks if tasks is not None else []
        self._id_profile = id_profile

    @property
    def id_schedule(self):
        return self._id_schedule

    @id_schedule.setter
    def id_schedule(self, id_schedule):
        self._id_schedule = id_schedule

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks if tasks is not None else []

    @property
    def id_profile(self):
        return self._id_profile

    @id_profile.setter
    def id_profile(self, id_profile):
        self._id_profile = id_profile