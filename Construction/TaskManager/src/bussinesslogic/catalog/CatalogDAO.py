from abc import ABC, abstractmethod
from dataaccess.DBConnection import DBConnection

class CatalogDAO(ABC):

    @abstractmethod
    def read_priority_catalog(self):
        pass

    @abstractmethod
    def read_status_catalog(self):
        pass