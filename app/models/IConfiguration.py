
from abc import ABC, abstractmethod

class IConfiguraton(ABC):
    @abstractmethod
    def __init__(self, params):
        pass
    @abstractmethod
    def get_config(self, query):
        pass
		