from typing import Iterable, Callable, Union, List
from src.urls import Url
from exceptions import NotFound, NotAllowed

from webob import Request, Response
from parse import parse


# class API:
#     def __init__(self):
#         self.routes = {}  # наши пути в связке ключ-значение, где ключ-строка, а значение - функция-обработчик
#
#     def route(self, path: str):
#         def wrapper(handler: Callable) -> Callable:
#             self.routes[path] = handler
#             return handler
#         return wrapper
#
#     def __call__(self, environ: dict, start_response) -> Iterable:
#         request = Request(environ)
#         response = self.handle_request(request)
#         return response(environ, start_response)
#
#     def handle_request(self, request: Request) -> Response:
#         response = Response()
#         handler, kwargs = self.find_handler(request_path=request.path)
#         if handler:
#             handler(request, response, **kwargs)
#         else:
#             self.default_response(response)
#         return response
#
#     def find_handler(self, request_path: str):
#         for path, handler in self.routes.items():
#             parse_result = parse(path, request_path)
#             if parse_result:
#                 return handler, parse_result.named
#         return None, None
#
#     def default_response(self, response: Response):
#         response.status_code = 404
#         response.text = "Not found."


class API:
    def __init__(self, urls: List[Url]):
        self.urls = urls

    def __call__(self, environ, start_response) -> Iterable:
        from pprint import pprint; pprint(environ)
        request_path = environ['PATH_INFO']
        handler = self.find_handler(request_path)()
        method = environ['REQUEST_METHOD'].lower()
        if not hasattr(handler, method):
            raise NotAllowed
        raw_response = getattr(handler, method)(None)  # получаем атрибут из класса
        response = raw_response.encode('utf-8')
        start_response('200 OK', [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response)))
        ])
        return iter([response])

    def find_handler(self, request_path: str):
        for path in self.urls:
            parse_result = parse(path.url, request_path)
            if parse_result:
                return path.view
        return NotFound


