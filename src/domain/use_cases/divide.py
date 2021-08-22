from abc import ABC, abstractmethod

from domain.dtos import DivideDTO

class Divide(ABC):

    @abstractmethod
    def calculate(self, params: DivideDTO):
        pass
