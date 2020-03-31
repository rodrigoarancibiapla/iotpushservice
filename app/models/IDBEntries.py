
from abc import ABC, abstractmethod

class IDBEntries(ABC):
    @abstractmethod
    def __init__(self, params):
        pass
    @abstractmethod
    def put_entry(self, data):
        pass
		