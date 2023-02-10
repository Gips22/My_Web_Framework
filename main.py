"""Файл входа с настройками."""
import os

from urls import urlpatterns
from src.api import API
from src.middleware import middlewares



"""Задание базовой директории для указания пути к файлам статики (CSS, JavaScript, изображения и т.д.).
Для указания пути к шаблонам.
Для указания пути к другим важным файлам, таким как настройки базы данных, конфигурационные файлы и т.д."""
settings = {
    'BASE_DIR': os.path.dirname(os.path.abspath(__file__)),  # базовая директория - папка корня проекта, где лежит текущий файл
}

app = API(
    urls=urlpatterns,
    settings=settings,
    middlewares=middlewares,
)
