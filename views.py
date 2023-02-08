"""Здесь уже пользовательские views"""
from src.view import View
from src.response import Response
from src.request import Request

class Home(View):
    def get(self, request: Request, *args, **kwargs):
        return Response(request, body='Привет! Это ГЛАВНАЯ страница')