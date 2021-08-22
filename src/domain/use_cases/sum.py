from abc import ABC, abstractmethod

from domain.dtos import SumDTO

class Sum(ABC):

    @abstractmethod
    def calculate(self, params: SumDTO):
        pass
