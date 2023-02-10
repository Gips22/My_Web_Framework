from typing import Iterable, Callable, Union, List, Type
from src.urls import Url
from exceptions import NotFound, NotAllowed
from src.request import Request

# from webob import Request, Response
from parse import parse
from src.response import Response
from src.middleware import BaseMiddleware


class API:
    def __init__(self, urls: List[Url], settings: dict, middlewares: List[Type[BaseMiddleware]]):
        self.urls = urls
        self.settings = settings
        self.middlewares = middlewares

    def __call__(self, environ: dict, start_response) -> Iterable:
        # from pprint import pprint; pprint(environ)
        handler = self._get_handle(environ)
        request = self._get_request(environ)
        self._middleware_to_request(request)
        response = self._get_response(environ, handler, request)  # получаем атрибут из класса
        self._middleware_to_response(response)
        start_response(str(response.status_code), response.headers.items())
        return iter([response.body])

    def find_handler(self, request_path: str):
        for path in self.urls:
            parse_result = parse(path.url, request_path)
            if parse_result:
                return path.view
        return NotFound

    def _get_handle(self, environ: dict):
        request_path = environ['PATH_INFO']
        handler = self.find_handler(request_path)()
        return handler

    def _get_request(self, environ: dict) -> Request:
        return Request(environ, self.settings)  # тут также пробрасываем settings из точки входа нашего приложения в request

    def _get_response(self, environ: dict, handler, request) -> Response:
        method = environ['REQUEST_METHOD'].lower()
        if not hasattr(handler, method):
            raise NotAllowed
        return getattr(handler, method)(request)

    def _middleware_to_request(self, request: Request):
        for i in self.middlewares:
            i().to_request(request)

    def _middleware_to_response(self, response: Request):
        for i in self.middlewares:
            i().to_response(response)




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
