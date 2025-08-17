from datetime import date, time

class Task:
    def __init__(
            self,
            id_task: int,
            title: str,
            status: str,
            priority: str,
            start_date: date,
            start_time: time,
            end_date: date,
            end_time: time,
            description: str,
            id_schedule: int
    ):
        self._id_task = id_task
        self._title = title
        self._status = status
        self._priority = priority
        self._start_date = start_date
        self._start_time = start_time
        self._end_date = end_date
        self._end_time = end_time
        self._description = description
        self._id_schedule = id_schedule

    @property
    def id_task(self):
        return self._id_task

    @id_task.setter
    def id_task(self, value):
        self._id_task = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def id_schedule(self):
        return self._id_schedule

    @id_schedule.setter
    def id_schedule(self, value):
        self._id_schedule = value

    def to_clean_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "priority": self.priority,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_date": self.end_date.isoformat() if self.end_date else None,
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "description": self.description,
            "id_schedule": self.id_schedule
        }