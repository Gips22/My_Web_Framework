from webob import Request, Response
from urls import urlpatterns
from src.api import API

app = API(urls=urlpatterns)


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
