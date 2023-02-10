from typing import Iterable, List

from parse import parse

from exceptions import NotFound, MethodNotAllowed
from src.response import Response
from src.middleware import Session
from src.request import Request
from src.urls import Url
from src.view import View


class API:
    def __init__(self, urls: List[Url], settings: dict, middlewares: List[Session]):
        self.urls = urls
        self.settings = settings
        self.middlewares = middlewares

    def __call__(self, environ: dict, start_response) -> Iterable:
        handler = self._get_handle(environ)
        request = self._get_request(environ)
        self._middleware_to_request(request)
        response = self._get_response(environ, handler, request)
        self._middleware_to_response(response)
        start_response(str(response.status_code), response.headers.items())
        return iter([response.body])

    def _get_handle(self, environ: dict) -> View:
        """Находим и возвращаем подходящую вьюху по URI"""
        request_path = environ['PATH_INFO']
        handler = self._find_handler(request_path)()
        return handler

    def _find_handler(self, request_path: str):
        """Вспомогательный метод для поиска вью. Если не находим - возвраащем NotFound"""
        for path in self.urls:
            parse_result = parse(path.url, request_path)
            if parse_result:
                return path.view
        return NotFound

    def _get_request(self, environ: dict) -> Request:
        return Request(environ, self.settings)  # тут также пробрасываем settings из точки входа нашего приложения в request

    def _get_response(self, environ: dict, handler, request) -> Response:
        """Возвращаем вьюху и передаем в нее request"""
        method = environ['REQUEST_METHOD'].lower()
        if not hasattr(handler, method):
            raise MethodNotAllowed
        return getattr(handler, method)(request)

    def _middleware_to_request(self, request: Request):
        """Оборачиваем request в middleware"""
        for middleware in self.middlewares:
            middleware().to_request(request)

    def _middleware_to_response(self, response: Request):
        """Оборачиваем response в middleware"""
        for middleware in self.middlewares:
            middleware().to_response(response)
