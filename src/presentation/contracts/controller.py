from abc import ABC, abstractmethod

from presentation.contracts import HttpRequest, HttpResponse

class HttpController(ABC):

    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse:
        pass
