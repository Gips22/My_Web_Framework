"""Здесь уже пользовательские views"""
from src.view import View

class Home(View):
    def get(self, request, *args, **kwargs):
        return "Привет! Это ГЛАВНАЯ страница"