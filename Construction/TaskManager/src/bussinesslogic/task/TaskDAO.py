from abc import ABC, abstractmethod

class TaskDAO(ABC):

    @abstractmethod
    def insert_json_task(self, task):
        pass

    @abstractmethod
    def read_json_task_by_title(self, id_task):
        pass

    @abstractmethod
    def read_tasks_by_schedule(self, id_schedule):
        pass

    @abstractmethod
    def read_json_tasks(self, id_shcedule):
        pass

    @abstractmethod
    def update_task(self):
        pass

    @abstractmethod
    def delete_task(self):
        pass

    @abstractmethod
    def conclude_task(self, task):
        pass