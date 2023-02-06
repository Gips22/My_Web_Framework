from typing import Iterable
from webob import Request, Response
import parse



# class API:
#     def __call__(self, environ: dict, start_response) -> Iterable:
#         response_body = b'{"Hello": "Word"}'
#         start_response(status="200", headers=[])
#         return iter([response_body])
#

class API:
    def __init__(self):
        self.routes = {}

    def route(self, path: str):
        debug_point = 1
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ: dict, start_response) -> Iterable:
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result:
                return handler, parse_result.named
        return None, None

    def handle_request(self, request: Request) -> Response:
        response = Response()
        handler, kwargs = self.find_handler(request_path=request.path)
        if handler:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def default_response(self, response: Response):
        """В случае отсутсвия обработчика для url- выдаем ошибку 404"""
        response.status_code = 404
        response.text = "Not found"