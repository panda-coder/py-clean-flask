from dataclasses import dataclass

@dataclass
class HttpRequest:
    params: dict
    body: dict

@dataclass
class HttpResponse:
    status: int
    body: dict