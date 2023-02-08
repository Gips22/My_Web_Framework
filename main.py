from urls import urlpatterns
from src.api import API
from src.middleware import middlewares
import os

"""Задание базовой директории lля указания пути к файлам статики (CSS, JavaScript, изображения и т.д.).
Для указания пути к шаблонам.
Для указания пути к другим важным файлам, таким как настройки базы данных, конфигурационные файлы и т.д."""

settings = {
    # 'BASE_DIR': os.path.dirname(os.path.abspath(__file__)), # базовая директория - папка корня проекта, где лежит текущий файл
    # 'TEMPLATES_DIR_NAME': 'templates'
}


app = API(
    urls=urlpatterns,
    settings=settings,
    middlewares=middlewares,
)

# @app.route(path="/home")
# def home(request: Request, response: Response):
#     response.text = "Привет! Это ГЛАВНАЯ страница"
#
#
# @app.route(path="/about")
# def about(request: Request, response: Response):
#     response.text = "Привет! Это страница О НАС!"
#
#
# @app.route(path="/hello/{name}")
# def greeting(request: Request, response: Response, name: str):
#     response.text = f"Hello, {name}"
