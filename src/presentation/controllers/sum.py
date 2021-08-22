
from presentation.contracts import HttpController, HttpRequest, HttpResponse
from domain.use_cases import Sum
from domain.dtos import SumDTO

class SumController(HttpController):
    def __init__(self, sum: Sum):
        super().__init__()
        self.sum = sum

    def handle(self, request: HttpRequest) -> HttpResponse:
        value = self.sum.calculate(SumDTO(**request.body))

        return HttpResponse(
            body={"value": value},
            status=200
        )
        