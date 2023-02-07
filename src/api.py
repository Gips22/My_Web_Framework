from typing import Iterable, Callable, Union

from webob import Request, Response
from parse import parse


class API:
    def __init__(self):
        self.routes = {}  # наши пути в связке ключ-значение, где ключ-строка, а значение - функция-обработчик

    def route(self, path: str):
        def wrapper(handler: Callable) -> Callable:
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ: dict, start_response) -> Iterable:
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self, request: Request) -> Response:
        response = Response()
        handler, kwargs = self.find_handler(request_path=request.path)
        if handler:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response

    def find_handler(self, request_path: str):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result:
                return handler, parse_result.named
        return None, None

    def default_response(self, response: Response):
        response.status_code = 404
        response.text = "Not found."
