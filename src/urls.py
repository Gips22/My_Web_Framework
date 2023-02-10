"""В этом модуле описывается стуктура URL"""
from dataclasses import dataclass
from typing import Type

from src.view import View


@dataclass
class Url:
    """Класс Url используется для определения соответствия между URL-адресом и соответствующим представлением."""
    url: str
    view: Type[View]
