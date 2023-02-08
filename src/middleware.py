"""Нужны чтобы добавлять значения которые нужны будут во views,
но их изначально нет в environ. К примеру, id пользователя в случае с авторизацией, аутентификацией"""
from src.request import Request
from src.response import Response
from uuid import uuid4
from urllib.parse import parse_qs


class Session:
    def to_request(self, request: Request):
        """Чтобы не обновлять при каждом запросе uuid делаем проверку."""
        cookie = request.environ.get('HTTP_COOKIE', None)
        if not cookie:
            return
        session_id = parse_qs(cookie)['session_id'][0]  # получаем id сессии
        request.extra['session_id'] = session_id

    def to_response(self, response: Response):
        if not response.request.session_id:
            response.update_headers(
                {"Set-Cookie": f"session_id={uuid4()}"}
            )

middlewares = [
    Session
]