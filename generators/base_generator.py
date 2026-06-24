from abc import ABC
from abc import abstractmethod

class BaseGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def save(self):
        pass