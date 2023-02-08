"""Нам придется передавать get параметры, id cессии и т.д.
Если передавать во View - будет каша, создаем отдельный (подобный dataclass) объект для этого"""
from urllib.parse import parse_qs


class Request:
    def __init__(self, environ, settings: dict):
        self.get_params(environ['QUERY_STRING'])
        self.settings = settings

    def get_params(self, raw_params: str):
        self.GET = parse_qs(raw_params)