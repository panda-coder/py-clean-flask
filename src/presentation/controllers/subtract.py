
from presentation.contracts import HttpController, HttpRequest, HttpResponse
from domain.use_cases import Subtract

from domain.dtos import SubtractDTO

class SubtractController(HttpController):
    def __init__(self, subtract: Subtract):
        super().__init__()
        self.subtract = subtract

    def handle(self, request: HttpRequest) -> HttpResponse:
        value = self.subtract.calculate(SubtractDTO(**request.body))

        return HttpResponse(
            body={"value": value},
            status=200
        )
        