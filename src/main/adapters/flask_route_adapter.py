from flask import Response
import json

from presentation.contracts import HttpController, HttpRequest

def adapt_route(flask_request, controller: HttpController):
    request = HttpRequest(
        params=flask_request.args,
        body=flask_request.json
    )
    data = controller.handle(request)
    return Response(
        json.dumps(data.body),
        status=data.status,
        mimetype='application/json'
    )
    try:
        request = HttpRequest(
            params=flask_request.args,
            body=flask_request.json
        )
        data = controller.handle(request)
        return Response(
            json.dumps(data.body),
            status=data.status,
            mimetype='application/json'
        )
    except Exception as e:
        return Response(
            json.dumps({"error": "Internal server error"}),
            status=500,
            mimetype='application/json'
        )
    
