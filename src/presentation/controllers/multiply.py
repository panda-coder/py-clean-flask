
from presentation.contracts import HttpController, HttpRequest, HttpResponse
from domain.use_cases import Multiply

from domain.dtos import MultiplyDTO

class MultiplyController(HttpController):
    def __init__(self, multiply: Multiply):
        super().__init__()
        self.multiply = multiply

    def handle(self, request: HttpRequest):
        value = self.multiply.calculate(MultiplyDTO(**request.body))

        return HttpResponse(
            body={"value": value},
            status=200
        )