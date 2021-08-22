
from domain.use_cases import Sum
from domain.dtos import SumDTO

class SumAction(Sum):

    def calculate(self, params: SumDTO):
        return params.x + params.y