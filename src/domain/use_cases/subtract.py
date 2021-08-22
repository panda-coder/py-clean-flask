from abc import ABC, abstractmethod

from domain.dtos import SubtractDTO

class Subtract(ABC):

    @abstractmethod
    def calculate(self, params: SubtractDTO):
        pass
