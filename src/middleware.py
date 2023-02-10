"""Middlewares нужны чтобы добавлять значения которые нужны будут во views,
но их изначально нет в environ. К примеру, id пользователя в случае с авторизацией.
Самое популярное - аутентификация"""
from uuid import uuid4

from urllib.parse import parse_qs

from src.request import Request
from src.response import Response


class Session:
    """Класс для привязки id к сессии пользоавтеля"""
    def to_request(self, request: Request) -> None:
        """Middleware, которой оборачиваем объект request.
        Чтобы не обновлять при каждом запросе идентификатор сессии, делаем проверку."""
        cookie = request.environ.get('HTTP_COOKIE', None)
        if not cookie:
            return
        session_id = parse_qs(cookie)['session_id'][0]  # получаем id сессии. parse_qs парсит строку кук и возвращает словарь.
        request.dict_for_cookies['session_id'] = session_id

    def to_response(self, response: Response) -> None:
        """Middleware, которой оборачиваем объект response.
        Если кука сессии отсутсвует-создаем и обновляем headers"""
        if not response.request.session_id:
            response.update_headers(
                {"Set-Cookie": f"session_id={uuid4()}"}
            )


middlewares = [Session]
