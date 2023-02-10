"""Отдельный модуль, содержащий класс View для абстрагирования и унификации поведения классов,
которые будут использоваться в качестве представлений (Views)."""
from src.response import Response, Request


class View:
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass
