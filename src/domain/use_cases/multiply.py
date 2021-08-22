from abc import ABC, abstractmethod

from domain.dtos import MultiplyDTO

class Multiply(ABC):

    @abstractmethod
    def calculate(self, params: MultiplyDTO):
        pass
