"""Нужны чтобы добавлять значения которые нужны будут во views,
но их изначально нет в environ. К примеру, id пользователя в случае с авторизацией.Самое популярное - аутентификация"""
from src.request import Request
from src.response import Response
from uuid import uuid4
from urllib.parse import parse_qs


class BaseMiddleware:

    def to_request(self, request: Request):
        return

    def to_response(self, response: Response):
        return


class Session:
    def to_request(self, request: Request):
        """Чтобы не обновлять при каждом запросе uuid делаем проверку."""
        print(f'Start func request, uuid = {uuid4}')
        cookie = request.environ.get('HTTP_COOKIE', None)
        if not cookie:
            return
        session_id = parse_qs(cookie)['session_id'][0]  # получаем id сессии
        request.extra['session_id'] = session_id
        print(request.extra)

    def to_response(self, response: Response):
        print(f'Start func response, uuid = {uuid4}')
        print(response.request.session_id)
        if not response.request.session_id:
            response.update_headers(
                {"Set-Cookie": f"session_id={uuid4()}"}
            )


middlewares = [
    Session
]
