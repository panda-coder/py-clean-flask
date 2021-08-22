
from domain.use_cases import Divide
from domain.dtos import DivideDTO

class DivideAction(Divide):

    def calculate(self, params: DivideDTO):
        return params.x / params.y