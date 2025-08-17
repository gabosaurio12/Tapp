from abc import ABC, abstractmethod

class ScheduleDAO(ABC):

    @abstractmethod
    def insert_schedule(self, schedule):
        pass
        
    @abstractmethod
    def read_schedule_by_profile(self, profile):
        pass

    @abstractmethod
    def read_schedule_id_by_profile(self, profile):
        pass

    @abstractmethod
    def update_schedule_by_id(self, schedule_id):
        pass

    @abstractmethod
    def delete_schedule_by_id(self, schedule_id):
        pass
