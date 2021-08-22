
from presentation.contracts import HttpController, HttpRequest, HttpResponse
from domain.use_cases import Divide

from domain.dtos import DivideDTO

class DivideController(HttpController):
    def __init__(self, divide: Divide):
        super().__init__()
        self.divide = divide

    def handle(self, request: HttpRequest):
        value = self.divide.calculate(DivideDTO(**request.body))

        return HttpResponse(
            body={"value": value},
            status=200
        )