
from domain.use_cases import Subtract
from domain.dtos import SubtractDTO

class SubtractAction(Subtract):

    def calculate(self, params: SubtractDTO):
        return params.x - params.y