from abc import ABC, abstractmethod

class ProfileDAO(ABC):

    @abstractmethod
    def insert_profile(self, profile):
        pass

    @abstractmethod
    def read_profile_by_username(self, username):
        pass

    @abstractmethod
    def read_profiles(self):
        pass

    @abstractmethod
    def update_profile_by_username(self, profile):
        pass

    @abstractmethod
    def delete_profile_by_username(self, username):
        pass
    