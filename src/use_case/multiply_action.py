
from domain.use_cases import Multiply
from domain.dtos import MultiplyDTO

class MultiplyAction(Multiply):

    def calculate(self, params: MultiplyDTO):
        return params.x * params.y