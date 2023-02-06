from typing import Iterable


def app(environ: dict, start_response) -> Iterable:
    """Параметры environ и start_response это объекты, которые передает нам Gunicorn.
    Environ - содержит параметры запроса. start_response нужен для формирования ответа"""
    response_body = b'{"Hello": "Word"}'
    start_response(status="200", headers=[])

    return iter([response_body])
