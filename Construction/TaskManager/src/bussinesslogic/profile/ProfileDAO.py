from abc import ABC, abstractmethod

class ProfileDAO(ABC):

    @abstractmethod
    def insert_profile(self, profile):
        pass

    @abstractmethod
    def read_profile_by_username(self, username):
        pass

    @abstractmethod
    def read_profile_by_id(self, id):
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

    @abstractmethod
    def update_current_profile(self, id):
        pass

    @abstractmethod
    def read_current_profile(self):
        pass

    @abstractmethod
    def get_hashed_password(self, password):
        pass
    