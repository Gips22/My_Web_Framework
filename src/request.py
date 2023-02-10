"""Cоздаем отдельный (подобный dataclass) объект Request. Чтобы не передавать get параметры, id cессии во View"""
from urllib.parse import parse_qs


class Request:
    def __init__(self, environ, settings: dict):
        self.get_params(environ['QUERY_STRING'])
        self.settings = settings
        self.environ = environ
        self.GET = None
        self.dict_for_cookies = {}

    def __getattr__(self, item):
        return self.dict_for_cookies.get(item, None)

    def get_params(self, raw_params: str):
        self.GET = parse_qs(raw_params)
