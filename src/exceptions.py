"""Кастомные исключения"""


class NotFound(Exception):
    code = 404
    text = 'Page not found'


class MethodNotAllowed(Exception):
    code = 405
    text = 'HTTP-method not supported'